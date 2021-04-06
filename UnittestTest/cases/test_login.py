#类来实现测试用例
import unittest, time
from selenium import webdriver

#登录模块
class TestCaseLogin(unittest.TestCase):

    #每个成员方法就是固定的测试用例
    def test_01_login_success(self):
        driver = webdriver.Chrome(executable_path="drivers\\chromedriver.exe")
        driver.maximize_window()  
        driver.get("http://127.0.0.1:8080/ljindex/index.html")      
        driver.find_element_by_link_text("登录").click()
        time.sleep(3)

        driver.find_element_by_id("username").send_keys("kakkg")
        driver.find_element_by_id("password").send_keys("12345678")
        driver.find_element_by_id("userLogin").click()

        #断言
        time.sleep(2)
        # assert driver.title == "测谈网"  #判断是否登录成功跳转到首页测谈网
        self.assertEqual(driver.title, "测谈网")  #表示两个值是否相等,跟上面一样
        driver.quit()
    # def test_02_suib(self):

    #     self.assertEqual(1, 2)


