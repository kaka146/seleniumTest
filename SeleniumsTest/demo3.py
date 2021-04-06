from selenium import webdriver
from seleniumtools import find_element

driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.maximize_window()
driver.get("https://passport2.eastmoney.com/pub/login?backurl=https%3A//www.eastmoney.com/")

#切换作用域到frame
# frame = ("id","frame_login")
# e = find_element(driver,frame)
# driver.switch_to_frame(e)

#点击密码登录
password_login = ("xpath",'/html/body/div/div[1]/span[1]')
find_element(driver,password_login).click()

username = ("id","txt_account")
find_element(driver,username).send_keys("15273459999")

#作用域切换回父网页
driver.switch_to_default_content()

mianfei = ("link text","点此进入基金交易")
find_element(driver, mianfei).click()