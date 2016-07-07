#encoding:utf-8
#读取testcase excel文件，获取测试数据，调用interfaceTest方法，将结果保存至errorCase列表中。
#read_excel.py
import xlrd, hashlib, json
import os, logging, sys

def runTest(testCaseFile):
      testCaseFile = os.path.join(os.getcwd(), testCaseFile)
      if not os.path.exists(testCaseFile):
          logging.error('测试用例文件不存在！')
          sys.exit()
      testCase = xlrd.open_workbook(testCaseFile)
      table = testCase.sheet_by_index(0)
      errorCase = []                #用于保存接口返回的内容和HTTP状态码
      s = None
      for i in range(1, table.nrows):
            if table.cell(i, 9).value.replace('\n','').replace('\r','') != 'Yes':
                print "11111"
                continue
            num = str(int(table.cell(i, 0).value)).replace('\n','').replace('\r','')
            api_purpose = table.cell(i, 1).value.replace('\n','').replace('\r','')
            api_host = table.cell(i, 2).value.replace('\n','').replace('\r','')
            request_method = table.cell(i, 4).value.replace('\n','').replace('\r','')
            request_data_type = table.cell(i, 5).value.replace('\n','').replace('\r','')
            request_data = table.cell(i, 6).value.replace('\n','').replace('\r','')
            encryption = table.cell(i, 7).value.replace('\n','').replace('\r','')
            check_point = table.cell(i, 8).value

            if encryption == 'MD5':              #如果数据采用md5加密，便先将数据加密
                print "encryption>>>>>>>>"
                request_data = json.loads(request_data)
                request_data['pwd'] = md5Encode(request_data['pwd'])
            status, resp, s = interfaceTest(num, api_purpose, api_host, request_url, \
              request_data, check_point, request_methon, request_data_type, s)
            if status != 200 or check_point not in resp:            #如果状态码不为200或者返回值中没有检查点的内容，\
                                                                    #那么证明接口产生错误，保存错误信息。
                errorCase.append((num + ' ' + api_purpose, str(status), 'http://' + api_host + request_url, resp))
            return errorCase

      print s



runTest("V1.4.5bug.xls")

