#encoding:utf-8
import xml.dom.minidom
import unittest
#from pyscopg2
#import requests
from xml_parse import *
class AppTestCase(unittest.TestCase):
	def __init__(self, filename):
		self.filename = 'config_ele.xml'
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
		self.info_username = CONF.get('app_info', 'username')
		self.info_passwd = CONF.get('app_info', 'passwd')
		self.packagename = CONF.get('app_info', 'packagename')
		self.udid = CONF.get('app_info', 'UDID')
		self.sender = CONF.get('email', 'sender')
		self.receiver = CONF.get('email', 'receiver')
		self.smtpserver = CONF.get('email', 'smtpserver')
		self.email_username = CONF.get('email','username')
		self.email_passwd = CONF.get('email', 'passwd')
	def setup(self):
		return 


	def teardown(self):
		self.close()

	def run(self):
		suite = unittest.TestSuite()
    	


def test_apprequest(self):
	testcase()


	
if __name__ == '__main__':
	filename = 'config_ele.xml'

	