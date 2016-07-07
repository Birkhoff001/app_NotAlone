#encoding:utf-8
#client_http.py
import requests
from PIL import Image
#from StringIO import StringIO
import json
import os
from set_config import CONF
from requests import Request, Session
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

class ClientRequests():
	def __init__(self):
		self.connection()

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

		#do something with prepped.body and prepped.headers
		resp = s.send(prepped, timeout=10)
		#print resp.status_code
		r_1 = requests.get('http://httpbin.org/stream/20', stream=True)
		#print dir(json)
		'''
		for line in r_1.iter_lines():
			if line:
				print json.loads(line)
		'''
		#pro = {"http": "http://10.10.1.10:3128", "https": "http://10.10.1.10:1080"}
		#requests.get("http://example.org", proxies=pro)		
		TOO_LONG = 50
		r_bing = requests.get('http://bing.com')
		#print r_bing.headers
		r_opt = requests.options('http://httpbin.org/stream/20')
		#print r_opt.headers
		if int(r_bing.headers['Content-Length']) < TOO_LONG:
			content = r.content
			#print content
		requests.Response.close(r_1)

		'''
		url11 = 'http://pan.baidu.com/disk/home#list/path=%2F%E6%88%91%E7%9A%84%E8%B5%84%E6%BA%90'
		r_2 = requests.get('http://some.url/streamed')
		print r_2.text
		with open('ccccc.py') as f:
			requests.post(url11, data=f)
		'''
		p_size = os.path.getsize('greece.jpg')
		p1_size = os.path.getsize('face.jpg')
		t1 = Image.open('greece.jpg')
		t2 = Image.open('face.jpg')
		#print "p_size:%s, p1_size:%s, t1_format:%s, t1_size:%s, t2_format:%s, t2_size:%s" % (p_size, p1_size, \
			#t1.format, t1.size, t2.format, t2.size) 
		multiple_files = [('images', ('greece.jpg', open('greece.jpg', 'rb'), 'image/jpg')), \
						('images', ('weibo.png', open('weibo.png', 'rb'), 'image/png'))]
		r_3 = requests.post(url2, files=multiple_files)
		
		#print r_3.text
	#requests.get('http://httpbin.org', hooks=dict(response=test_requests))
	#hooks = dict(response=test_requests())
	#requests.post('http://some.url/streamed', data=test_requests())
		#url_head = 'https://api.github.com/users/kennethreitz/repos?page=1&per_page=10'
		#head_ = requests.head(url=url_head)
		#print head_.headers(['link'])

class PizzaAuth(AuthBase):
	def __init__(self, username):
		self.username = None

	def __call__(self, r):
		self.r.headers['X-Pizza'] = self.username
		return r
		print requests.get('http://pizzabin.org/admin', auth=PizzaAuth('kenneth'))

		'''
		auth = HTTPBasicAuth('fake@example.com', 'not_a_real_password')
		body = json.dumps({u"body": u"Sounds great! I'll get right on it!"})
		url_auth = u"https://api.github.com/repos/kennethreitz/requests/issues/482/comments"
		r_auth = requests.post(url=url_auth, data=body, auth=auth)
		print r_auth.status_code
		content = r_auth.json()
		print (content[u'body'])
		#print help(requests.post)
		#print "auth-------\n", help(auth), '\n'
		'''
if __name__ == '__main__':
	url = 'https://github.com/timeline.json'
	ClientRequests(url)
	PizzaAuth(AuthBase)
	




