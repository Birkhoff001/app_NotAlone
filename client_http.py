#encoding:utf-8
#client_http.py
import requests
from PIL import Image
import unittest
#from StringIO import StringIO
import json
import os
from set_config import CONF
from requests import Request, Session
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

class ClientRequests(unittest.TestCase):
	def setUp(self):
		self.conn = connection()

	def tearDown(self):
		self.conn.disponse()
		self.conn = None

	def connection(self):
		try:
			s = requests.Session()
			s_1 = s.get(self.url, data=send_data(headers))
			print "connection status:", s_1.status_code, s_1.headers
		except Exception, e:
			print e

	#def send_data(self, data_header ):
		#return

	def check_data(self, _headers):
		_headers = {
		"Http_x_bd_subsys":"apimap",
		"Http_x_bd_product":"map",
		"Transfer-Encoding":"chunked",
		"Set-Cookie":"",
		"Expires":"",
		"Http_x_bd_logid":"3491563439",
		"Server":"apache",
		"Http_x_bd_logid64":"11857827200559218017",
		"Content-Type":"application/octet-stream;charset=utf-8"
		}
		

	def test_requests(self):
		url = 'https://www.bing.com'
		#print dir(requests)
		#print dir(requests.Response)
		url1 = 'https://github.com/timeline.json'
		url2 = 'http://httpbin.org/post'
		url3 = 'http://httpbin.org/delete'
		url4 = 'http://httpbin.org/head'
		url5 = 'http://httpbin.org/get'
		url6 = 'http://api.map.baidu.com/api?x=13529482&y=3639980&qt=rgc&bt=0&extf=0&mb=iPhone8%2C1&os=iphone9.3.2&sv=2.7.0&net=1&resid=02&cuid=569969c8c0fe7bca95de589240819efd&channel=faild&pcn=com.younotalone.younotalone&ap'
		url7 = 'http://mmbiz.qpic.cn/mmbiz/\j9ZVwzSMxKPVlrZKOvcfsykGGKNiclmjufOx6EYiaIXz6PvicUJTORCbYcrLR9oWyq2e19sTm6GeYz2JCerxg3tSg/0?wx_fmt=png/0'
		url8 = 'http://example.com/some/cookie/setting/url'
		url9 = 'http://httpbin.org/cookies'
		url10 = 'https://github.com/kennethreitz/requests/tarball/master'
		url11 = 'https://api.github.com/repos/kennethreitz/requests/git/commits/a050faf084662f3a352dd1a941f2c7c9f886d4ad'
		payload = {'appname':'notalone', 'version':'v1.1.0'}
		payload1 = {'appname':'notalone'}
		payload2 = {'test':'v1.1.0'}
		try:
			r = requests.get(url6, timeout=1)
			s = requests.Session()
			#s.auth('test':'123')
			s.get("http://httpbin.org/cookies")
			r1 = s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
			#s.headers.update({'test':'22222'})
			print r.headers
			if r.status_code == requests.codes.ok:
				print r.headers['Content-Security-Policy']
			print r1.status_code, '\n'
			r_json = r.json()
			#print r_json.keys
		except Exception, e:
			print e

		filename = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app_setting.conf')

		s = Session()
		req = Request('GET', url2, data=payload1, headers=payload2)
		prepped = s.prepare_request(req)
		resp = s.send(prepped, timeout=10)
		r_1 = requests.get('http://httpbin.org/stream/20', stream=True)	
		TOO_LONG = 50
		r_bing = requests.get('http://bing.com')
		#print r_bing.headers
		r_opt = requests.options('http://httpbin.org/stream/20')
		#print r_opt.headers
		if int(r_bing.headers['Content-Length']) < TOO_LONG:
			content = r.content
			#print content
		requests.Response.close(r_1)

		p_size = os.path.getsize('greece.jpg')
		p1_size = os.path.getsize('face.jpg')
		t1 = Image.open('greece.jpg')
		t2 = Image.open('face.jpg')
		#print "p_size:%s, p1_size:%s, t1_format:%s, t1_size:%s, t2_format:%s, t2_size:%s" % (p_size, p1_size, \
			#t1.format, t1.size, t2.format, t2.size) 
		multiple_files = [('images', ('greece.jpg', open('greece.jpg', 'rb'), 'image/jpg')), \
						('images', ('weibo.png', open('weibo.png', 'rb'), 'image/png'))]
		r_3 = requests.post(url2, files=multiple_files)

class ClientRequestsSuite(unittest.TestSuite):
	def __init__(self):
		unittest.TestSuite.__init__(self, map(ClientRequests, "test_requests"))


if __name__ == '__main__':
	ClientRequestsSuite()
	unittest.TextTestRunner(verbosity=2).run(ClientRequestsSuite)
	#suite = unittest.TestLoader().loadTestsFromTestCase(ClientRequests)
    #unittest.TextTestRunner(verbosity=2).run(suite)





