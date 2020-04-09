import unittest
from test_case import MyTest
import time
global driver

class OrderPage(unittest.TestCase):
    def setUp(self):
        MyTest.setUp(self)
    def tearDown(self):
        MyTest.tearDown(self)
    def inorderpage(self):
        '''进入下单系统页面'''
        driver = self.driver
        driver.get(self.base_url + '/')
        MyTest.login(self)
        driver.find_element_by_xpath(".//*[@id='root']/div/div[1]/div[1]/div/ul/li[11]/div[1]").click()  # 点击在线下单系统
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='root']/div/div[1]/div[1]/div/ul/li[11]/ul/li[1]/a").click()#进入下单系统页面
        time.sleep(2)
    def inspecificationwindow(self):
        OrderPage.inorderpage(self)
        driver = self.driver
        # product=driver.find_elements_by_xpath('.//*[@class="ant-row"]/div')
        driver.find_element_by_xpath(
            ".//*[@id='root']/div/div[1]/div[2]/div[2]/div/div[3]/div/div/div/div/div[1]/div/div/div/ul/li[2]/span/i").click()
        time.sleep(2)
class AddCartTest(unittest.TestCase):
    '''在线下单-加入购物车'''
    def setUp(self):
        MyTest.setUp(self)
    def tearDown(self):
        MyTest.tearDown(self)
    def test_inorderpage(self):
        '''在线下单-进入下单系统'''
        OrderPage.inorderpage(self)
    def test_editspecification_in(self):
        '''在线下单，加入购物车-进入产品下单规格选择'''
        OrderPage.inspecificationwindow(self)
        driver = self.driver
        txt=driver.find_element_by_id('rcDialogTitle0').text
        self.assertEqual(txt,'产品下单规格选择')
    def test_editspecification_default(self):
        '''在线下单，加入购物车-产品下单规格选择默认的'''
        OrderPage.inspecificationwindow(self)
        driver = self.driver
        driver.find_element_by_xpath('.//*[@class="ant-modal-footer"]/div/button[2]').click()
