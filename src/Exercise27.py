#!/usr/bin/env python3

"""
利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
"""


def reduce_print(s):
    if len(s) == 1:
        return s
    else:
        return reduce_print(s[1:]) + s[0]


print(reduce_print('abcde'))
