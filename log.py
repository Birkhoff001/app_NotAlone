#encoding:utf-8
#record_log.py
import logging,os

def log_func():
	log_file = os.path.join(os.getcwd(),'./test.log')
	log_format = '[%(asctime)s] [%(levelname)s] %(message)s'    
	logging.basicConfig(format=log_format, filename=log_file, filemode='w', level=logging.DEBUG)
	console = logging.StreamHandler()
	console.setLevel(logging.DEBUG)
	formatter = logging.Formatter(log_format)
	console.setFormatter(formatter)
	logging.getLogger('').addHandler(console)

LOG = log_func()