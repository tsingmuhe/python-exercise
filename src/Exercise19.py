#!/usr/bin/env python3

"""
一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
"""
from functools import reduce


def factor_arr(num):
    arr = [1]
    for i in range(2, num):
        if num % i == 0:
            arr.append(i)
    return arr


for i in range(2, 1001):
    arr = factor_arr(i)
    totalSum = reduce(lambda x, y: x + y, arr)
    if i == totalSum:
        print("%d = " % i, end='')
        print(arr)
