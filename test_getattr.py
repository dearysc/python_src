#!/usr/bin/python
# -*- coding:utf-8 -*-

''' this module is used to test '__getattr__'function!'''

class Student(object):
	def __init__(self,name):
		self.name = name
	
	def __getattr__(self,attr):
		if attr == 'score':
			return 95

