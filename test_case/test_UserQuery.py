import csv
import unittest
import time
from test_case import MyTest

class UserRole(unittest.TestCase):

    def setUp(self):
        MyTest.setUp(self)
    def tearDown(self):
        MyTest.tearDown(self)
    def insystemmanagement(self):
        '''进入用户角色管理页面'''
        driver=self.driver
        driver.get(self.base_url + '/')
        MyTest.login(self)
        driver.find_element_by_xpath(".//*[@id='root']/div/div[1]/div[1]/div/ul/li[10]/div/span/span").click()  # 点击系统管理
        time.sleep(2)
        driver.find_element_by_xpath(".//*[@id='root']/div/div[1]/div[1]/div/ul/li[10]/ul/li[1]/a").click()
        time.sleep(2)
class UserQueryTest(unittest.TestCase):
    '''用户角色管理-查询'''
    def setUp(self):
        MyTest.setUp(self)
    def tearDown(self):
        MyTest.tearDown(self)
    def test_insystemmanagement(self):
        '''用户角色管理-进入用户列表'''
        UserRole.insystemmanagement(self)
    def test_userquery_username(self):
        '''用户角色管理-用户名查询存在的用户'''
        UserRole.insystemmanagement(self)
        my_file = '../file/user.csv'  # 测试用户登陆调用数据的地址
        date = csv.reader(open(my_file, 'r', errors='ignore'))  # 'r'为读取模式
        for user in date:
            if user[3]=='账号密码正确':
                username=user[0]
                driver = self.driver
                driver.find_element_by_id('username').send_keys(username)
                driver.find_element_by_id('username').submit()
                print('搜索用户名：'+username)
                result=driver.find_element_by_class_name('ant-table-tbody')
                u=result.find_element_by_xpath('tr[1]/td[3]').text
                print('搜索结果第一行的用户名：'+u)
                try:
                    self.assertEqual(u, username)
                    print('搜索成功')
                except:
                    print('搜索失败')
                self.assertEqual(u, username)
                driver.refresh()
    def test_userquery_username_error(self):
        '''用户角色管理-用户名查询查询不存在的用户'''
        UserRole.insystemmanagement(self)
        my_file = '../file/user.csv'  # 测试用户登陆调用数据的地址
        date = csv.reader(open(my_file, 'r', errors='ignore'))  # 'r'为读取模式
        for user in date:
            if user[3]=='账号错误':
                username=user[0]
                driver = self.driver
                driver.find_element_by_id('username').send_keys(username)
                driver.find_element_by_id('username').submit()
                print(username)
                result=driver.find_element_by_class_name('ant-table-placeholder').text
                print(result)
                try:
                    self.assertEqual(result, '暂无数据')
                    print('搜索结果提示正确')
                except:
                    print('搜索失败')
                self.assertEqual(result, '暂无数据')
                driver.refresh()
    def test_userquery_phone(self):
        '''用户角色管理-手机号查询存在的手机号的用户'''
        UserRole.insystemmanagement(self)
        my_file = '../file/user.csv'  # 测试用户登陆调用数据的地址
        date = csv.reader(open(my_file, 'r', errors='ignore'))  # 'r'为读取模式
        for user in date:
            if user[5]=='用户对应的手机号正确':
                phone=user[4]
                driver = self.driver
                driver.find_element_by_id('phone').send_keys(phone)
                driver.find_element_by_id('phone').submit()
                print('搜索手机号：'+phone)
                result=driver.find_element_by_class_name('ant-table-tbody')
                u=result.find_element_by_xpath('tr[1]/td[6]').text
                print('搜索结果第一行手机号：'+u)
                try:
                    self.assertEqual(u, phone)
                    print('搜索成功')
                except:
                    print('搜索失败')
                self.assertEqual(u, phone)
                driver.refresh()
    """
    def test_userquery_phone_error(self):
        '''用户角色管理-手机号查询，手机错误'''
        UserRole.insystemmanagement(self)
        my_file = '../file/user.csv'  # 测试用户登陆调用数据的地址
        date = csv.reader(open(my_file, 'r', errors='ignore'))  # 'r'为读取模式
        for user in date:
            if user[5]=='手机号错误':
                phone=user[4]
                driver = self.driver
                driver.find_element_by_id('phone').send_keys(phone)
                driver.find_element_by_id('phone').submit()
                print('搜索手机号：'+phone)
    """
