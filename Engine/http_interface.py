#encoding:utf-8
#accept runTest's parameter，use requests creat HTTP request

import requests

def interfaceTest(num, api_purpose, api_host, request_method, request_data_type, request_data, check_point, s=None):
     headers = {'Content-Type' : 'application/x-www-form-urlencoded; charset=UTF-8',
                      'X-Requested-With' : 'XMLHttpRequest',
                      'Connection' : 'keep-alive',
                      'Referer' : 'http://' + api_host,
                      'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) \ppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36'
                }

     if s == None:
          s = requests.session()
     if request_method == 'POST':
          if request_url != '/login' :
              r = s.post(url='http://'+api_host+request_url, \
              data = json.loads(request_data), headers = headers)         #data has no encryption,so need decode Json charactor change to python objects.
          elif request_url == '/login' :
              s = requests.session()
              r = s.post(url='http://'+api_host+request_url, \
              data = request_data, headers = headers)                     #used MD5 encryption，the before codes have been changed to json.loads()，so no need to encryption.
          else:
              logging.error(num + ' ' + api_purpose + '  HTTP请求方法错误，请确认[Request Method]字段是否正确！！！')
              s = None
              return 400, resp, s
     status = r.status_code
     resp = r.text
     print resp
     if status == 200 :
        if re.search(check_point, str(r.text)):
            logging.info(num + ' ' + api_purpose + ' 成功，' + str(status) + ', ' + str(r.text))
            return status, resp, s
        elif:
            logging.error(num + ' ' + api_purpose + ' 失败！！！，[' + str(status) + '], ' + str(r.text))
            return 200, resp , None
        else:
            logging.error(num + ' ' + api_purpose + '  失败！！！，[' + str(status) + '],' + str(r.text))
            return status, resp.decode('utf-8'), None




