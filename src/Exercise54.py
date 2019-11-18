#!/usr/bin/env python3

"""
取一个整数a从右端开始的4〜7位。。
"""
a = int(input('input a number:'))
print(bin(a))
b = 0b1111
print(a & b)
print(bin(a & b))
