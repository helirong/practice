from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys

class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.base_url="http://10.10.0.146:8100/"
    def tearDown(self):
        self.driver.quit()
    def login(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_id("username").send_keys("admin")
        driver.find_element_by_id("password").send_keys("123456")
        driver.find_element_by_id("password").submit()
        time.sleep(2)
    def system(self):
        driver = self.driver
        MyTest.login(self)
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='root']/div/div[1]/div[1]/div/ul/li[10]/div[1]").click()  # 点击系统管理
    def order(self):
        driver = self.driver
        MyTest.login(self)
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='root']/div/div[1]/div[1]/div/ul/li[11]/div[1]").click()  # 点击在线下单系统

    def inproduct(self):
        driver = self.driver
        MyTest.login(self)
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='root']/div/div[1]/div[1]/div/ul/li[4]/div[1]").click()  # 点击产品管理
        #driver.find_element_by_class_name("ant-menu ant-menu-dark ant-menu-root ant-menu-inline").find_element_by_xpath('li[4]/div[1]/span/span').click()
        time.sleep(2)
    def inseries(self):
        driver = self.driver
        MyTest.login(self)
        #MyTest.inproduct(self)
        driver.find_element_by_xpath(".//*[@id='root']/div/div[1]/div[1]/div/ul/li[4]/div").click()
        time.sleep(2)
        driver.find_element_by_link_text("产品系列管理").click()
        time.sleep(2)
    def inclassify(self):
        driver = self.driver
        MyTest.login(self)
        #MyTest.inproduct(self)
        driver.find_element_by_xpath(".//*[@id='root']/div/div[1]/div[1]/div/ul/li[4]/div").click()  # 点击产品管理
        time.sleep(2)
        driver.find_element_by_link_text("产品分类管理").click()  # 进入系列管理页面
        time.sleep(2)
    def inlist(self):
        driver = self.driver
        MyTest.login(self)
        MyTest.inproduct(self)
        #driver.find_element_by_xpath(".//*[@id='root']/div/div[1]/div[1]/div/ul/li[4]/div").click()  # 点击产品管理
        time.sleep(2)
        driver.find_element_by_link_text("产品列表").click()  # 进入产品列表页面
        time.sleep(2)
    def queryeditproduct(self):
        driver = self.driver
        # 搜索测试专用产品，产品编号：4500010012
        driver.find_element_by_xpath(
            ".//*[@id='root']/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/form/div/div[4]/span/button[2]").click()
        driver.find_element_by_id("code").send_keys("4500010012")
        driver.find_element_by_xpath(
            ".//*[@id='root']/div/div[1]/div[2]/div[2]/div/div[2]/div/div/div/div[1]/form/div/div[4]/span/button[1]").click()
        time.sleep(1)


if __name__=="__main__":
    unittest.main()