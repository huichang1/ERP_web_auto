# print("陈灰常")
# print("李灰常")
# # print("东灰常")

# name = input("请输入姓名：")
# age = input("请输入年龄：")
# gender = input("请输入性别：")
#
# print ('''*******************
# 姓名：%s
# 年龄：%s
# 性别：%s
# *******************'''%(name,age,gender))

# str1 = 'hello world!'
# print ("A" in str1)
# print (str1.count("o"))
# a = 10
# b = 5
# a -=3
# print ( a + b )

# amount = input("请输入金额:")
# print ('''金额：{}'''.format(amount))

# dict_1={"class_id":45, 'num' :20}
# if dict_1.get("num") > 5 :
#     print ( dict_1.get("num") )
# else :
#     print ("上课人数不足6人")

# count = 0
# list1 = ["方方土","七木","荷花鱼","kingo","Amiee","焕蓝"]
# print (type(list1))
# dict1 = dict(list1)
# # for name in list1:
# #     if name == "方方土" :
# #         list1.insert(0,('"gender":"female"','"age":"18"','"city":"guangzhou"'))
# #         continue
# print (dict1)
# #     print ("*"*20)
#     count += 1
# print (count)

# list1 = ['方方土', '七木', '荷花鱼', 'kingo', 'Amiee', '焕蓝']
# value0 = "gender:female,age:18,city:Guangzhou"
# value1 = "gender:male,age:10,city:Shenzhen"
# value2 = "gender:male,age:28,city:Changsha"
# value3 = "gender:female,age:52,city:Wuhan"
# value4 = "gender:male,age:31,city:Chengdu"
# value5 = "gender:female,age:83,city:Beijing"
# list2 = [value0,value1,value2,value3,value4,value5]
# list3 =zip(list1,list2)
# dict1 = dict(list3)
# print (dict1)

# list1 = ["方方土","七木","荷花鱼","kingo","Amiee","焕蓝"]
# name1 = input("请输入姓名：")
# dict1 = {"方方土":1,"七木":2,"荷花鱼":3,"kingo":4,"Amiee":5,"焕蓝":6}
# dict1["方方土"] = "gender:female,age:18,city:Guangzhou"
# dict1["七木"] = "gender:male,age:10,city:Shenzhen"
# dict1["荷花鱼"] = "gender:male,age:28,city:Changsha"
# dict1["kingo"] = "gender:female,age:52,city:Wuhan"
# dict1["Amiee"] = "gender:male,age:31,city:Chengdu"
# dict1["焕蓝"] = "gender:female,age:83,city:Beijing"
# for name in dict1:
#     if name == name1:
#         print(dict1.get(name))
# print("*"*20)
# print (dict1)
# print("*"*20)
# list2=list(dict1.keys())
# list3=list(dict1.values())
# print (list2,list3)

# str = "hui","小小","1","Ture"
# list1 = list(str)
# print (list1)

# list = ["1","kingdom","灰常","False","1.098","a+b+c",[3,4,5,6],{1,2,3,4}]  # 列表
# len1 = len(list)
# print("长度:{}".format(len1))
# int1 = int(len1)
# print ("元素个数:{}".format(int1))
# if int1 > 5:
#     print (True)
# else:
#     print (False)

# str = "kingdom"  # 字符串
# len1 = len(str)
# print("长度:{}".format(len1))
# int1 = int(len1)
# print ("元素个数:{}".format(int1))
# if int1 > 5:
#     print (True)
# else:
#     print (False)
# sum = 0
# for i in range(0,101,2):
#     sum += i
#     print(i)
# print ("0-100中偶数的总和：{}".format(sum))

# dict1 = {"name":"John","age":"1","city":"GZ","weigeht":"89KG"}
# # len1 = len(dict1)
# # print (len1)

# money = 1000
# if money > 5000:
#     print ("买别墅！")
# elif money > 3000:
#     print("买跑车！")
# elif money > 2000:
#     print("买玩具车！")
# else:
#     print ("穷鬼，该去赚钱了")
# count = 0
# list1 = ["1","kingdom","灰常","False","1.098",{1,2,3,4}]
# for name in list1:       # for 变量名  in 数据对象：（冒号缩进）
#     if name == "灰常":   #      子代码（循环体）
#         continue            # continue==>只跳出本次循环
#     print(name)
#     print("*" * 20)
#     count += 1
#     print ("循环第几次：{}".format(count))
# print ("list1的长度是多少？（元素个数）：{}".format(len(list1)))

# for i in range(2,12,3):     # 序列：1、2、3、4、5、6、7、8、9、10.....
#     print (i)

# def good_job(salary,bonus,subsidy=500,*args,**kwargs):
#     sum1 = salary + bonus + subsidy
#     print ("salary的值：{}".format(salary))
#     print ("bonus的值：{}".format(bonus))
#     print ("subsidy的值：{}".format(subsidy))
#     print("args的值：{}".format(args))
#     print("kwargs的值：{}".format(kwargs))
#     for i in args:
#         sum1 += i
#     for j in kwargs:
#         sum1 += kwargs.get(j)
#     print ("这个工作的工作总和是：{}".format(sum1))
# good_job(8000, subsidy=800, bonus=2000,aa=50, bb=100)

# def good_job():              # def  函数名():   ===>定义函数名
# #     salary = 8000            # 子代码（函数体）===》实现功能
# #     bonus = 2000
# #     subsidy = 500
# #     sum1 = salary + bonus + subsidy
# #     print ("这个工作的工作总和是：{}".format(sum1))
# #     return sum1   #定义了一个返回值，若定义多个返回值，用英文逗号隔开，Ex：return sum1,salary
# # result = good_job()   # 调用————通过result的变量接收返回值
# # print (result)
# # if result > 10000:
# #     print ("这是一份好工作！")
# # else:
# #     print ("增值技能，找一份更好的！")

import time   #导入这个time模块——Python自带的
# from selenium import webdriver   #从selenium工具导入webdriver库
# driver = webdriver.Chrome()      #选择Chrome，初始化driver==》可以浏览器进行沟通，建立会话session
# driver.get("http://erp.lemfix.com/login.html") #打开一个网址driver.get("url")
# driver.maximize_window() # 浏览器窗口最大化driver.maximize_windows()
# time.sleep(3)   #延时操作time.sleep(数字)
# driver.forward()  #向前进driver.forward()
# time.sleep(3)  #延时操作time.sleep(数字)
# driver.back()  #向后退driver.back()
# time.sleep(3)  #延时操作time.sleep(数字)
# driver.refresh()  # 刷新driver.refresh()
# driver.find_element_by_id("username").send_keys("test123")   #找到了有username这个id的元素
# driver.find_element_by_id("password").send_keys("123456")    #找到了有password这个id的元素
# driver.find_element_by_id("btnSubmit").click()            #点击有btnSubmit这个id的元素

# driver.find_element_by_name("username").send_keys("test123")   #找到了有username这个name的元素
# driver.find_element_by_name("password").send_keys("123456")    #找到了有password这个name的元素
# driver.find_element_by_id("btnSubmit").click()            #点击有btnSubmit这个id的元素

# username = driver.find_element_by_xpath('//input[@id="username"]').send_keys("test123")
# print ("username")
# page_text = driver.find_element_by_xpath('//div[@class="login-logo"]//b').text
# page_text = driver.find_element_by_xpath('//b[text()="柠檬ERP"]').text
# page_text = driver.find_element_by_xpath('//b[contains(text(),"柠檬ERP")]').text
# page_text = driver.find_element_by_xpath('//input[contains(@id,"username")]').send_keys("test123")
from selenium import webdriver   #从selenium工具导入webdriver库
driver = webdriver.Chrome()      #选择Chrome，初始化driver==》可以浏览器进行沟通，建立会话session
driver.get("http://erp.lemfix.com/login.html") #打开一个网址driver.get("url")
driver.maximize_window() # 浏览器窗口最大化driver.maximize_windows()
driver.find_element_by_id("username").send_keys("test123")   #找到了有username这个id的元素
driver.find_element_by_id("password").send_keys("123456")    #找到了有password这个id的元素
driver.find_element_by_id("btnSubmit").click()            #点击有btnSubmit这个id的元素
driver.implicitly_wait(5)   #隐式等待5s：从登陆页面切换成点击"零售出库"的页面
driver.find_element_by_xpath('//span[text()="零售出库"]').click()  #点击"零售出库"的切换页面
# 通过id的属性来定位iframe
P_id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
print (P_id)
# 通过拼接的方式来赋值给新的id2
F_id = P_id + "-frame"
# 1）把获取的字符串，switch_to转换为frame
# driver.switch_to.frame(F_id)
# 2）通过xpath的元素定位来切换iframe
# driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@id='{}']".format(F_id)))
# 3) 通过iframe下标的方式来切换iframe，从0开始表示主页面，1：下一级页面，2：下下级页面
driver.switch_to.frame(1)
print (F_id)
# 向单据编号的搜索框输入314的值
driver.find_element_by_xpath('//input[@id="searchNumber"]').send_keys("314")  #方法一：xpath相对路径的方法
driver.find_element_by_id("searchNumber").send_keys("314")   #方法二：id属性的定位方法
driver.find_element_by_name("searchNumber").send_keys("314")  #方法三：name属性的定位方法
# # 点击查询按钮(xpath的文本属性定位）
# driver.find_element_by_xpath('//span[text()="查询"]').click()
# time.sleep(2)  #强制性等待，防止出现元素没加载完就取获取值
# # 判断搜索的单据订单号是否一致
# # 1、定位搜索结果的单据编号
# danjubianhao = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
# print (danjubianhao)
# # 2、比对这两个单据编号是否一致
# if "314" in danjubianhao:
#     print ("通过测试！")
# else:
#     print ("不通过测试！")