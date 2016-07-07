#encoding:utf=8
import email
import smtplib
from email.mime.text import MIMEText
from email.header import Header
#import set_config
from set_config import CONF 
import base64
import os
class Email_report:
	def __init__(self, txtname):
		print "-------------start--------------"
		try:
			with open(txtname, 'rb') as conf_file_fp:
				CONF.readfp(conf_file_fp)
		except Exception, e:
			print e 

		self.ip = CONF.get('server', 'ip')
		self.port = CONF.get('server', 'port')
		self.httpport = CONF.get('server', 'httpport')
		self.url = CONF.get('server', 'url')
		self.dbname = CONF.get('database', 'dbname')
		self.dbuser = CONF.get('database', 'dbuser')
		self.dbhost = CONF.get('database', 'dbhost')
		self.version = CONF.get('app_info', 'version')
		self.devices = CONF.get('app_info', 'devices')
		self.appname = CONF.get('app_info', 'appname')
		self.info_username = CONF.get('app_info', 'user')
		self.info_passwd = CONF.get('app_info', 'passwd')
		self.packagename = CONF.get('app_info', 'packagename')
		self.udid = CONF.get('app_info', 'UDID')
		self.sender = CONF.get('email', 'sender')
		self.receiver = CONF.get('email', 'receive')
		self.smtpserver = CONF.get('email', 'smtpserver')
		self.email_username = CONF.get('email','username')
		self.email_passwd = CONF.get('email', 'passwd')
		self.email_port = CONF.get('email', 'port')
		self.msg = CONF.get('email', 'msg')
		self.email_func_unserver()

	'''
	def email_func():
		sender = CONF.get('email', 'sender')
		receivers = CONF.get('email', 'receive')
		message = MIMEText('send email test=====', 'plain', 'utf=8')
		message['From'] = Header("cainiao learning", 'utf=8')
		message['To'] = Header("Test", 'utf=8')

		subject = 'SMTP email test'
		message['Subject'] = Header(subject, 'utf=8')


		try:
		    smtpObj = smtplib.SMTP('localhost')
		    smtpObj.sendmail(sender, receivers, message.as_string())
		    print "Email send successful!"
		except smtplib.SMTPException, e:
			print "Error: ", e
	'''
	def email_func_unserver(self):
		message = {}
		try:
			with open(self.msg, 'w') as msg_f:
				f = CONF.readfp(msg_f)
			print "woca --*****", f
			print message.append(f)
		except Exception, e:
			print e 
		print message

		try:
		    smtpObj = smtplib.SMTP()
		    print smtpObj.set_debuglevel(2)
		    print "connect===================="
		    smtp_conn = smtpObj.connect(host=self.smtpserver, port=self.email_port)
		    print smtp_conn
		    smtp_starttls = smtpObj.starttls(keyfile=None, certfile=None)
		    print smtp_starttls
		    print "login=================="
		    smtp_login = smtpObj.login(self.email_username, self.email_passwd)
		    print smtp_login
		    print "sendmail================="
		    smtp_sendmail = smtpObj.sendmail(self.sender, self.receiver, self.msg)
		    print smtp_sendmail
		    print "---------From: " + self.sender + " To: " + self.receiver + \
		    " email send successful!--------"
		    smtpObj.quit()
		    print "SMTPserver closed==================="
		    return True
		except smtplib.SMTPException, e:
			print "Error: ", e
			return False
		
if __name__ == '__main__':
	#email_func()
	txtname = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app_setting.conf')
	Email_report(txtname)
