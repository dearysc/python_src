#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys,os
import requests
import urllib
#reload(sys)
#sys.setdefaultencoding('utf-8')

print u'中文测试'
print 'scottyuan'
print 'juliehwang'

url = 'http://www.baidu.com'

res = requests.get(url)
print res.status_code
