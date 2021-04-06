#注册自动化
from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("http://127.0.0.1:8080/ljindex/")


driver.find_element_by_xpath('//*[@id="unlogin"]/div[2]/a').click()
time.sleep(3)
driver.find_element_by_id('username').send_keys("kakknng")
driver.find_element_by_id('phonenum').send_keys("15273455748")
driver.find_element_by_id('password').send_keys("12345678")
driver.find_element_by_id('confirpw').send_keys("12345678")
driver.find_element_by_id('emailnum').send_keys("12345678@qq.com")
time.sleep(2)
driver.find_element_by_id('userRegist').click()

time.sleep(3)
#弹出窗
driver.switch_to_alert().accept() #移动到弹窗提示语 .点击确定按钮

try:
    assert driver.title =="登录"
    print("注册成功")
except:
    print("注册失败")