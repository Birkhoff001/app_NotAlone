import xml.dom.minidom
def xml_parser(self, filename='test_config.xml'):
	#filename = 'config_ele.xml'
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

def insert_sort(lists):
	count = len(lists)
	for i in range(1, count):
		key = lists[i]
		j = i - 1
		while j >= 0:
			if lists[j] > key:
				lists[j+1] = lists[j]
				lists[j] = key
			j -= 1
		print "insert_sort:----", lists
	return lists

def shell_sort(lists1):
	count = len(lists1)
	step = 2
	group = count/step
	while group > 0:
		for i in range(0, group):
			j = i + group
			while j < count:
				k = j - group
				key = lists1[j]
				while k >= 0:
					if lists1[k] > key:
						lists1[k + group] = lists1[k]
						lists1[k] = key
					key -= group
				j += group
		group /= step
		print "shell_sort:---", lists1
	print "shell_sort:---", lists1
	return lists
	

def bubble_sort(lists2):
	count = len(lists2)
	for i in range(0, count):
		for j in range(i+1, count):
			if lists2[i] > lists2[j]:
				lists2[i], lists2[j] = lists2[j], lists2[i]
			print "bubble_sort:---", lists2
	return lists

filename = 'test_config.xml'
lists = [1, 4, 6, 7, 2, 3, 0]
lists1 = [44, 11, 22, 55, 33]
lists2 = [44, 11, 22, 55, 33]
#xml_parser(filename)
insert_sort(lists)
shell_sort(lists1)
bubble_sort(lists2)
