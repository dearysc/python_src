#!/usr/bin/python
# -*- coding:utf-8 -*-
"this is a power module!"
def power(x,n=2):
	s = 1
	while n>0:
		s = s*x
		n = n-1
	return s

if __name__ == '__main__':
	print power(3)
	print power(5,3)
