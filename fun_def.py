#!/usr/bin/python
from functools import partial,wraps
import sys,os


def decorate_new(auth='required'):
    def decorate_f(f):
        @wraps(f)
        def wrap(*args,**kwargs):
            print('scottyuan')
            return f(*args,**kwargs)
        return wrap
    return decorate_f

@decorate_new(auth="optional")
def my_add(x):
	'apply + operation to argument'
	return x+x

print(my_add(15))
