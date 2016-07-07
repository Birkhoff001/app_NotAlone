#encoding:utf-8
import xlrd
import os

'''
class TestCaseExcel:
	def __init__(self, fname):
		self.fname = os.path.join('./123.xls')

def __init__(self, fname):
	self.fname = "123.xls"
'''
fname = "123.xls"
def read_excl(fname):
	try:
		open_f = fname.open_workbook()
		excl_range = range(open_f)
		print excl_range
		return open_f
	except Exception, e:
		print str(e)

def get_table_byname(fname, col_index=0, col_name=u'Sheet1'):
	data = read_excl(fname)
	table = data.sheet_by_name(col_name)
	nrows = table.nrows
	ncols = table.ncols
	row_values = table.row_values(col_index)
	#col_values = table.col_values()
	print nrows, ncols
	list = []
	for rownum in range(1, nrows):
		row = table.row_values(rownum)
		if row:
			t = {}
			for i in range(len(row_values)):
				t[row_values[i]] = row[i]
			list.append(t)
	return list

def func():
	tables = get_table_byname(fname)
	for row in tables:
		print row


if __name__ == '__main__':
	func()
