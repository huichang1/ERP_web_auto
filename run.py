from qcd import Python_erp   #导入封装函数文件
from test_data import test_data   #导入测试数据文件
from selenium import webdriver  # 从selenium工具导入webdriver库
driver = webdriver.Chrome()  # 选择Chrome，初始化driver==》可以浏览器进行沟通，建立会话session
driver.implicitly_wait(5)
#调用函数
url = test_data.url["url"] #取值url
user = test_data.login_data["username"]   #取值登录用户名
pwd = test_data.login_data["password"]   #取值登录密码
s_key = test_data.s_key["s_key"]    #取值 搜索的 关键字
print (url,user,pwd,s_key)
#调用函数  ——传参
#给函数定义一个返回值——调用函数的时候用一个变量result接收返回值
result = Python_erp.search_key(driver=driver, url=url, username=user, password=pwd, s_key=s_key)
if s_key in result:
    print ("单据编号一致")
else:
    print ("测试用例不通过！")