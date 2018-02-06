# -*- coding: utf-8 -*-
def func(a, b=5, c=10):
    print('a равно {a}, b равно {b}, c равно {c}'.format(a=a, b=b, c=c))

func(3,7)
func(25, c=145)
func(c=12,b=11,a=10)