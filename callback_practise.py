#encoding:utf-8

def _generator():
	print "starting up---"
	yield 1
	print "working ---"
	yield 2
	print "working still--"
	yield 3

for i in _generator():
	print i


def __generator():
	print "starting up twice--"
	yield 1
	print "working twice---"
	yield 2
	print "working still twice--"
	yield 3

gen = __generator()


while True:
	try:
		g = gen.next()
	except StopIteration:
		break
	else:
		print g





