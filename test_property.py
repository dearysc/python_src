#!/usr/bin/python 
# -*- coding:utf-8 -*-

'''
	this module is used to test 'propery' work, and 
	how does this method turn a function to a attribute!
'''

class Parrot(object):
	def __init__(self):
		self.__voltage = 100
		self.__current = 15
	
	@property
	def voltage(self):
		return self.__voltage

	@property
	def current(self):
		return self.__current

	@voltage.setter
	def voltage(self,value):
		if (not isinstance(value,float)) and (not isinstance(value,int)):
			raise ValueError('voltage must be a float!')
		if value <0 or value >220:
			raise ValueError('voltage must between 0~220V!')
		self.__voltage = value

	@voltage.deleter
	def voltage(self):
		del self.__voltage

	@current.setter
	def current(self,value):
		if (not isinstance(value,float)) and (not isinstance(value,int)):
			raise TypeError('Current type must be float!')
		if value < 0 or value > 10:
			raise ValueError('current must between 0~10A!')
		self.__current = value

	@current.deleter
	def current(self):
		del self.__current


if __name__ == '__main__':
	a = Parrot()
	print 'normal test!'
	a.voltage = 55.0
	a.current = 7.0
	

