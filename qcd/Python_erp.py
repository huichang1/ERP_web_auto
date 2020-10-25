# from selenium import webdriver  # 从selenium工具导入webdriver库
# driver = webdriver.Chrome()  # 选择Chrome，初始化driver==》可以浏览器进行沟通，建立会话session
import time
def login_page (username,password,driver):  #形参 --参数化--提高代码复用率
    driver.find_element_by_id("username").send_keys(username)  # 找到了有username这个id的元素
    driver.find_element_by_id("password").send_keys(password)  # 找到了有password这个id的元素
    driver.find_element_by_id("btnSubmit").click()
def open_url (url,driver):
    driver.get(url)  # 打开一个网址driver.get("url")
    driver.maximize_window()  # 浏览器窗口最大化driver.maximize_windows
def search_key(url,driver,username,password,s_key):
  open_url (url,driver)
  login_page (username,password,driver)
  driver.implicitly_wait(5)   #隐式等待5s：从登陆页面切换成点击"零售出库"的页面
  driver.find_element_by_xpath('//span[text()="零售出库"]').click()  #点击"零售出库"的切换页面
  P_id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
  # 通过拼接的方式来赋值给新的id2
  F_id = P_id + "-frame"
  # 1）把获取的字符串，switch_to转换为frame
  # driver.switch_to.frame(F_id)
  # 2）通过xpath的元素定位来切换iframe
  # driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(F_id)))
  # 3) 通过iframe下标的方式来切换iframe，从0开始表示主页面，1：下一级页面，2：下下级页面
  driver.switch_to.frame(1)
  # 向单据编号的搜索框输入314的值
  driver.find_element_by_xpath('//input[@id="searchNumber"]').send_keys(s_key)  # 方法一：xpath相对路径的方法
  # 点击查询按钮(xpath的文本属性定位）
  driver.find_element_by_xpath('//span[text()="查询"]').click()
  time.sleep(2)  #强制性等待，防止出现元素没加载完就取获取值
  # 1、定位搜索结果的单据编号
  num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
  return num  #返回值
  # 2、比对这两个单据编号是否一致
  # if s_key in num:
  #     print ("通过测试！")
  # else:
  #     print ("不通过测试！")