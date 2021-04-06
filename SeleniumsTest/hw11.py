import time
from selenium import webdriver
from seleniumtools import find_element  #用的自定义的动态查找方法
#用包装类的driver.implicitly_wait(10) 显示等待 注册自动化

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("http://127.0.0.1:8080/ljindex")

usrername = ("id","username")  #用户输入框
phonenum = ("id","phonenum")
password = ("id","password")
confirpw = ("id","confirpw")
emailnum = ("id","emailnum")
userRegist = ("id","userRegist") 
zhuce = ("link text",'注册') #注册输入框 

# zhuce = ("xpath",'//*[@id="collapsibleNavId"]/div[3]/div/button[2]/span')
# zhanghao = ("xpath",'//*[@id="Register"]/div[2]/div[2]/div/form/div[1]/div/div/input')
# mima = ("xpath",'//*[@id="Register"]/div[2]/div[2]/div/form/div[2]/div/div/input')

find_element(driver, zhuce).click() #点击注册页面按钮
# find_element(driver,zhanghao).send_keys("15273455748")

find_element(driver, usrername).send_keys("kakkangs")    #输入用户名
find_element(driver, phonenum).send_keys("15273455748")
find_element(driver, password).send_keys("12345678")     #输入密码
find_element(driver, confirpw).send_keys("12345678")     #确认密码
find_element(driver, emailnum).send_keys("123@qq.com")   #输入邮箱
find_element(driver, userRegist).click()                 #点击确认注册 

