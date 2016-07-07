#encoding:utf-8
import hashlib 
from MD5_data import lorem
h = hashlib.md5()
#print dir(h)
#print help(h.update)
h.update(lorem)
#print lorem
print h.hexdigest()

