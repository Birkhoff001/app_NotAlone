import xml.dom.minidom

filename = 'config_ele.xml'
dom = xml.dom.minidom.parse(filename)
root = dom.documentElement
testcases = root.getElementsByTagName('Testcases')
testcase = []
for childNode in testcases:
	testcase.append(childNode)
print testcase
print type(dom)
print type(root)
print type(testcases)
print dir(testcases)

