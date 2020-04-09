import unittest
import time
from HTMLTestRunner import HTMLTestRunner
#discover()方法自动根据测试目录（test_case）匹配查找测试用例文件（test*.py）
from framework.SendEmail import SendMail

discover=unittest.TestLoader().discover("test_case")
if __name__=="__main__":
    #按照一定格式获取当前时间
    now=time.strftime("%Y-%m-%d %H-%M-%S")

    #定义报告存放路径
    filename='../report/'+now+'result.html'
    fp=open(filename,'wb')

    #始化一个HTMLTestRunner实例对象，用来生成报告
    runner=HTMLTestRunner(stream=fp,title='浪度大数据营销平台测试报告',description='用例执行情况')
    #执行测试套件
    runner.run(discover)
    #fp.close()
    # 测试结束之后，执行邮件发送报告
    sendMail = SendMail()
    sendMail.send()
