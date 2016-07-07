#encoding:utf-8
import hashlib
import smtplib
import email
import unittest

def md5Encode(data):
      hashobj = hashlib.md5()
      hashobj.update(data.encode('utf-8'))
      return hashobj.hexdigest()

def sendMail(text):
      mail_info = get_conf()
      sender = mail_info['sender']
      receiver = mail_info['receiver']
      subject = '[AutomationTest]接口自动化测试报告通知'
      smtpserver = mail_info['smtpserver']
      username = mail_info['username']
      password = mail_info['passwd']
      msg = MIMEText(text,'html','utf-8')
      msg['Subject'] = subject
      msg['From'] = sender
      msg['To'] = ''.join(receiver)
      smtp = smtplib.SMTP()
      smtp.connect(smtpserver)
      smtp.login(username, password)
      smtp.sendmail(sender, receiver, msg.as_string())
      smtp.quit()


def main():
      errorTest = runTest('Case_Src/V1.4.5bug.xls')
      if len(errorTest) > 0:
          html = '<html><body>接口自动化扫描，共有 ' + str(len(errorTest)) + ' 个异常接口，列表如下：' + \
          '</p><table><tr><th style="width:100px;text-align:left">接口</th><th style="width:50px;text-align:left">状态</th><th style="width:200px;text-align:left">接口地址</th><th   style="text-align:left">接口返回值</th></tr>'
          for test in errorTest:
              html = html + '<tr><td style="text-align:left">' + test[0] + '</td><td style="text-align:left">' + \
              test[1] + '</td><td style="text-align:left">' + test[2] + '</td><td style="text-align:left">' + test[3] \
              + '</td></tr>'
              sendMail(html)

if __name__ == '__main__':
    #md5Encode(data)
    #sendMail(text)
    main()

