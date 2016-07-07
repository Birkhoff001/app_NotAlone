#encoding:utf-8
import ConfigParser
from ConfigParser import SafeConfigParser
import os
import sys

def get_config():
	config = SafeConfigParser()
	#print dir(ConfigParser)
	conffile_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app_setting.conf')
	#print conffile_path + '\n'
	with open(conffile_path, 'rb') as conf_file_fp:
		config.readfp(conf_file_fp)
	return config
'''
def get_conf(confname):
    conf_file = ConfigParser.ConfigParser()

    conf_file.read(os.path.join(os.getcwd(), confname))

    conf = {} 

    return conf
'''	
get_config()
CONF = get_config()
#print dir(CONF)

