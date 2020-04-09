import unittest
import time
import csv
import xlrd
from selenium.webdriver import ActionChains
from test_case import MyTest

class LoginTest(unittest.TestCase):
    """登陆测试"""
    def setUp(self):
        MyTest.setUp(self)
    def test_login_normal(self):
        """登陆测试-账号密码正确"""
        my_file = '../file/user.csv'#测试用户登陆调用数据的地址
        filePath='../file/User-login-test-results.csv'#用户登陆的测试结果写入的地方
        #filePath = '../file/User-login-test-results.xlsx'  # 用户登陆的测试结果写入的地方
        date = csv.reader(open(my_file, 'r', errors='ignore'))#'r'为读取模式
        driver = self.driver
        driver.get(self.base_url + "/")
        for user in date:
            if user[3]=='账号密码正确':
                username = user[0]
                password = user[1]
                state =user[2]
                date=user[3]
                print('测试登陆用户:' + username + ',' + password)
                driver.find_element_by_id("username").send_keys(username)
                driver.find_element_by_id("password").send_keys(password)
                driver.find_element_by_id("password").submit()
                time.sleep(2)
                title = driver.title
                try:
                    self.assertEqual(title,"管理驾驶舱 - 浪度家居互联网营销平台")
                    result='登陆测试成功'
                    driver.quit()
                    MyTest.setUp(self)
                    driver = self.driver
                    driver.get(self.base_url + "/")
                    '''
                    print(role+result)
                    # 定位到要悬停的元素
                    above = driver.find_element_by_xpath(".//*[@id='root']/div/div[1]/div[2]/div[1]/div/div/span[2]")
                    # 对定位到的元素进行悬停操作
                    ActionChains(driver).move_to_element(above).perform()
                    # 定位到悬停后要点击的元素
                    element = driver.find_elements_by_class_name("ant-dropdown-menu-item")[4]
                    element.click()
                    time.sleep(2)
                    '''
                except:
                    result = '登陆测试失败'
                    print(state  + result)
                    driver.refresh()
                self.assertEqual(title, "管理驾驶舱 - 浪度家居互联网营销平台")
                # 按照一定格式获取当前时间
                now = time.strftime("%Y-%m-%d %H-%M-%S")
                # 将测试结果写入到‘../file/User-login-test-results.csv’
                csvFile2 = open(filePath, 'a', newline='')  # 打开要写入到的文件,设置newline，否则两行之间会空一行，'a'为追加模式，不会覆盖掉之前的数据
                # writer = xlrd.writer(csvFile2,dialect='excel')#定义一个变量进行写入，将刚才的文件变量传进来，dialect就是定义一下文件的类型，我们定义为excel类型
                writer = csv.writer(csvFile2)
                writer.writerow([date, state, username, password, result, now])
                time.sleep(2)
    def test_login_name_error(self):
        """登陆测试-账号错误"""
        my_file = '../file/user.csv'  # 测试用户登陆调用数据的地址
        filePath = '../file/User-login-test-results.csv'  # 用户登陆的测试结果写入的地方
        date = csv.reader(open(my_file, 'r', errors='ignore'))  # 'r'为读取模式
        driver = self.driver
        driver.get(self.base_url + "/")
        for user in date:
            if user[3] == '账号错误':
                username = user[0]
                password = user[1]
                state = user[2]
                date = user[3]
                print('测试登陆用户:' + username + ',' + password)
                driver.find_element_by_id("username").send_keys(username)
                driver.find_element_by_id("password").send_keys(password)
                driver.find_element_by_id("password").submit()
                time.sleep(2)
                errorusernamehint = driver.find_element_by_xpath("html/body/div[2]/div/span/div/div/div/span").text
                print(errorusernamehint)
                try:
                    self.assertEqual(errorusernamehint, username + " 不存在")
                    result='提示正确'
                except:
                    print('提示错误')
                self.assertEqual(errorusernamehint, username + " 不存在")
                # 按照一定格式获取当前时间
                now = time.strftime("%Y-%m-%d %H-%M-%S")
                # 将测试结果写入到‘../file/User-login-test-results.csv’
                csvFile2 = open(filePath, 'a', newline='')  # 打开要写入到的文件,设置newline，否则两行之间会空一行，'a'为追加模式，不会覆盖掉之前的数据
                # writer = xlrd.writer(csvFile2,dialect='excel')#定义一个变量进行写入，将刚才的文件变量传进来，dialect就是定义一下文件的类型，我们定义为excel类型
                writer = csv.writer(csvFile2)
                writer.writerow([date,state , username, password, result, now])
                time.sleep(2)
                driver.refresh()
                time.sleep(2)
    def test_login_password_error(self):
        """登陆测试-密码错误"""
        my_file = '../file/user.csv'  # 测试用户登陆调用数据的地址
        filePath = '../file/User-login-test-results.csv'  # 用户登陆的测试结果写入的地方
        date = csv.reader(open(my_file, 'r', errors='ignore'))  # 'r'为读取模式
        driver = self.driver
        driver.get(self.base_url + "/")
        for user in date:
            if user[3] == '密码错误':
                username = user[0]
                password = user[1]
                state = user[2]
                date = user[3]
                print('测试登陆用户:' + username + ',' + password)
                driver.find_element_by_id("username").send_keys(username)
                driver.find_element_by_id("password").send_keys(password)
                driver.find_element_by_id("password").submit()
                time.sleep(2)
                text_errorpasswordhint = driver.find_element_by_xpath(
                    "html/body/div[2]/div/span/div/div/div/span").text
                print(text_errorpasswordhint)
                try:
                    self.assertEqual(text_errorpasswordhint, "用户名和密码不匹配")
                    result='提示正确'
                except:
                    print('提示错误')
                self.assertEqual(text_errorpasswordhint, "用户名和密码不匹配")
                # 按照一定格式获取当前时间
                now = time.strftime("%Y-%m-%d %H-%M-%S")
                # 将测试结果写入到‘../file/User-login-test-results.csv’
                csvFile2 = open(filePath, 'a', newline='')  # 打开要写入到的文件,设置newline，否则两行之间会空一行，'a'为追加模式，不会覆盖掉之前的数据
                # writer = xlrd.writer(csvFile2,dialect='excel')#定义一个变量进行写入，将刚才的文件变量传进来，dialect就是定义一下文件的类型，我们定义为excel类型
                writer = csv.writer(csvFile2)
                writer.writerow([date,state , username, password, result, now])
                time.sleep(2)
                driver.refresh()
                time.sleep(2)
    def test_login_null(self):
        """登陆测试-账号密码都为空"""
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.find_element_by_xpath(
            ".//*[@id='root']/div/div[1]/div[2]/div/form/div/div[3]/div/div/span/button").click()
        time.sleep(2)
        text_usernamehint = driver.find_element_by_xpath(
            ".//*[@id='root']/div/div[1]/div[2]/div/form/div/div[1]/div[2]/div[1]/div[1]/div/div/div").text
        print(text_usernamehint)
        print('账号为空:提示正确')
        text_passwordhint = driver.find_element_by_xpath(
            ".//*[@id='root']/div/div[1]/div[2]/div/form/div/div[1]/div[2]/div[1]/div[2]/div/div/div").text
        try:
            self.assertEqual(text_usernamehint, "请输入姓名")
            print('账号为空:提示正确')
            self.assertEqual(text_passwordhint, "请输入密码")
            print('密码为空:提示正确')
        except:
            print('账号密码都为空:提示错误')
        self.assertEqual(text_usernamehint, "请输入姓名")
        self.assertEqual(text_passwordhint, "请输入密码")
    def test_login_username_null(self):
        """登陆测试-账号为空"""
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.find_element_by_id("password").send_keys('123456')
        driver.find_element_by_id("password").submit()
        time.sleep(2)
        text_usernamehint = driver.find_element_by_xpath(
            ".//*[@id='root']/div/div[1]/div[2]/div/form/div/div[1]/div[2]/div[1]/div[1]/div/div/div").text
        print(text_usernamehint)
        try:
            self.assertEqual(text_usernamehint, "请输入姓名")
            print('账号为空:提示正确')
        except:
            print('账号为空:提示错误')
        self.assertEqual(text_usernamehint, "请输入姓名")
    def test_login_password_null(self):
        """登陆测试-密码为空"""
        driver = self.driver
        driver.get(self.base_url + '/')
        driver.find_element_by_id("username").send_keys('admin')
        driver.find_element_by_id("password").submit()
        time.sleep(2)
        text_passwordhint = driver.find_element_by_xpath(
            ".//*[@id='root']/div/div[1]/div[2]/div/form/div/div[1]/div[2]/div[1]/div[2]/div/div/div").text
        try:
            self.assertEqual(text_passwordhint, "请输入密码")
            print('密码为空:提示正确')
        except:
            print('密码为空:提示错误')
        self.assertEqual(text_passwordhint, "请输入密码")
    def tearDown(self):
        MyTest.tearDown(self)

if __name__=="__main__":
    unittest.main()