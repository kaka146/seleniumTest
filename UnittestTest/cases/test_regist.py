import unittest, time
from selenium import webdriver
from po.PageReg import PageRegist  #这里是导入这个文件的类
class TestCaseReg(unittest.TestCase):

    #类方法：setupclass/teardownclass
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path="drivers\\chromedriver.exe")
        cls.driver.maximize_window()  

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    #成员方法：setup/teardown
    def setUp(self):
        self.driver.get("http://127.0.0.1:8080/ljindex/index.html")
        self.driver.find_element_by_link_text("注册").click() 

    def test_01_reg_success(self):
        # self.driver.find_element_by_link_text("注册").click() 
        time.sleep(3)
        #去注册

    def test_02_reg_failed(self):
        # self.driver.find_element_by_link_text("注册").click() 
        time.sleep(3)
        #去注册

    def test_03_demo(self):
        """
            这是po对象的例子
        """
        reg = PageRegist(self.driver)
        reg.regist("zhangfei","12345678","12345678","15288888088","god@qq.com")