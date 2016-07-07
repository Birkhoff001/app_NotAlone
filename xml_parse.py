#encoding:utf-8
import xml.dom.minidom
from xml.etree import ElementTree as ET
class TestSuite:
	def __init__(self, fileName):
		dom = xml.dom.minidom.parse(fileName)
		root = dom.documentElement
		self.testcases = []
		testcaseNodes = root.getElementsByTagName("testcase")
		for testcaseNode in testcaseNodes:
			self.testcases.append(Testcase(testcaseNode))

class Testcase:
	def __init__(self, testcaseNode):
		self.name = testcaseNode.getAttribute('name')
		print "---%s Request----" % self.name
		self.requests = []
		requestNodes = testcaseNode.getElementsByTagName('Requests')
		for requestNode in requestNodes:
			self.requests.append(Request(requestNode))

class Request:
	def __init__(self, requestNode):
		self.url = requestNode.getAttribute('url')
		self.is_https = requestNode.getAttribute('is_https')
		self.http_method = requestNode.getAttribute('http_method')
		print "url:", self.url, " | ", "is_https:", self.is_https, " | ", "http_method:", self.http_method
		self.params = []
		paramNodes = requestNode.getElementsByTagName('param')
		for paramNode in paramNodes:
			self.params.append(Param(paramNode))
		self.signups = []
		signupNodes = requestNode.getElementsByTagName('signup')
		for signupNode in signupNodes:
			self.signups.append(Signup(signupNode))

class Param:
	def __init__(self, paramNode):
		self.key = paramNode.getAttribute('key')
		self.value = paramNode.getAttribute('value')
		print "key:%s" % self.key , " | ", "value:%s" % self.value 
	

class Signup:
	def __init__(self, signupNode):
		self.tel = signupNode.getAttribute('tel')
		self.telack = signupNode.getAttribute('telack')
		self.passwd = signupNode.getAttribute('passwd')
		self.signname = signupNode.getAttribute('signname')
		print "tel:", self.tel, " | ", "telack:", self.telack, " | ", "passwd:", self.passwd,\
		" | ", "signname:", self.signname

'''
	def app_requests(self, file='config_ele.xml'):
		per = ET.parse(file)
		p = per.findall('./Testcases')
		print p

		for ele_p in p:
			for child in ele_p.getchildren():
				print child.tag, ":", child.text

		pp = per.findall('./Testcases/Requests')
		print pp
		for ele_pp in pp:
			for child in ele_pp.getchildren():
				print child.tag, ":", child.text


#Init_Config(file)
#findAll_Config(file)

'''

if __name__ == '__main__':
	fileName = 'test_config.xml'
	TestSuite(fileName)
