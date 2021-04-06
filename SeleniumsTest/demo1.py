from selenium import webdriver
import time
#1、打开浏览器:固定的/ 获取浏览器的句柄

driver = webdriver.Chrome(executable_path='chromedriver.exe')

# #2、输入并且访问网址
driver.get("https://www.testgoup.com/#/")

driver.maximize_window()
time.sleep(3)

#3、开始操作网页
# xpath定位
e = driver.find_element_by_xpath('//*[@id="collapsibleNavId"]/div[3]/div/button[1]/span')
e.click()  #点击
time.sleep(5)
# time.sleep(3)
driver.find_element_by_xpath('//*[@id="pane-first"]/form/div[1]/div/div[1]/input').send_keys("15273455748")
driver.find_element_by_xpath('//*[@id="pane-first"]/form/div[2]/div/div[1]/input').send_keys("1653176507")
driver.find_element_by_xpath('//*[@id="Login"]/div[2]/div[2]/div/div/div/div[2]/button').click()
driver.quit()
#超链接
# driver.find_element_by_link_text("学术").click()
# driver.find_element_by_partial_link_text()
# id 定位
# driver.find_element_by_id("usrername").send_keys("15273455748")
# driver.find_element_by_id("password").send_keys("1653176507")
# driver.find_element_by_id("userLogin").click()
#文章 //*[@id="collapsibleNavId"]/ul/li[1]/a
#登录  //*[@id="collapsibleNavId"]/div[3]/div/button[1]/span 
#注册  //*[@id="collapsibleNavId"]/div[3]/div/button[2]/span

# driver.get("https://www.baidu.com/")
#通过name来定位
# driver.find_element_by_name("wd").send_keys("python")
#通过class来定位
# driver.find_element_by_class_name("s_ipt").send_keys("python")
#通过selector(跟xpath类似)来定位
# driver.find_element_by_css_selector("#kw").send_keys("python")

#推出去测试(推出浏览器)：driver.quit()
