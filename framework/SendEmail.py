# coding:utf-8

import os, sys
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#reportPath = 'E:\\xuexi\\test\\test_project - 1\\report'# 测试报告的路径
reportPath = '../report/'
print("打印路径：")

print(reportPath)


class SendMail(object):

    def get_report(self):  # 该函数的作用是为了在测试报告的路径下找到最新的测试报告

        dirs = os.listdir(reportPath)
        dirs.sort()
        newreportname = dirs[-1]
        print('The new report name: {0}'.format(newreportname))
        return newreportname  # 返回的是测试报告的名字

    def take_messages(self):  # 该函数的目的是为了 准备发送邮件的的消息内容
        newreport = self.get_report()
        self.msg = MIMEMultipart()
        self.msg['Subject'] = '浪度家居互联网营销平台自动化测试报告'  # 邮件的标题
        self.msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')

        with open(os.path.join(reportPath, newreport), 'rb') as f:
            mailbody = f.read()  # 读取测试报告的内容
        html = MIMEText(mailbody, _subtype='html', _charset='utf-8')  # 将测试报告的内容放在 邮件的正文当中
        self.msg.attach(html)  # 将html附加在msg里

        # html附件    下面是将测试报告放在附件中发送
        att1 = MIMEText(mailbody, 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'

        att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'  # 这里的filename可以任意写，写什么名字，附件的名字就是什么
        self.msg.attach(att1)

    def send(self):

       # recipients = ['xxxx@xxxx.com', 'xxxx@qq.com', 'xxx@xxxxx.com']  # 发送给多个人
        #recipients = ['443253143@qq.com'] #发送给一个人
        recipients = ['1668145067@qq.com']
        self.take_messages()
        self.msg['from'] = '1668145067@qq.com'  # 发送邮件的人，这种是公司邮箱转发
        #self.msg['to'] = recipients  # 收件人和发送人必须这里定义一下，执行才不会报错。
        toaddrs = recipients
        smtp = smtplib.SMTP()
        smtp.connect('smtp.qq.com')
        smtp.ehlo()
        smtp.login('1668145067@qq.com', 'ktkascnnmbumbihc')
        smtp.sendmail(self.msg['from'], toaddrs, self.msg.as_string())  # 发送邮件
        smtp.close()
        print('sendmail success')


if __name__ == '__main__':
    sendMail = SendMail()
    sendMail.send()