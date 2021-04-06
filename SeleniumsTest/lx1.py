from selenium import webdriver
import time
#最新的测谈网登录
driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.get("https://www.testgoup.com/#/")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="collapsibleNavId"]/div[3]/div/button[1]/span').click()

#等待三秒
time.sleep(3)

driver.find_element_by_xpath('//*[@id="pane-first"]/form/div[1]/div/div[1]/input').send_keys("15273455748")
driver.find_element_by_xpath('//*[@id="pane-first"]/form/div[2]/div/div[1]/input').send_keys("1653176507")
driver.find_element_by_xpath('//*[@id="Login"]/div[2]/div[2]/div/div/div/div[2]/button').click()

#断言
time.sleep(3)
# driver.implicitly_wait(10) 
try:
    assert driver.current_url == "https://www.testgoup.com/"
    print("登录成功")
except:
    print("登录失败")
