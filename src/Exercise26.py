#!/usr/bin/env python3

"""
利用递归方法求5!。
"""


def reduce_cal(num):
    if num == 1:
        return 1
    else:
        return num * reduce_cal(num - 1)


print(reduce_cal(5))
