#!/usr/bin/env python3

"""
将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
"""
from math import sqrt


def reduce_num(num):
    arr = [1]
    while num != 0:
        tmp = reduce_num_1(num)
        arr.append(tmp)
        num = num // tmp
    return arr


def reduce_num_1(num):
    end = int(sqrt(num + 1))
    for i in range(2, end + 1):
        if num % i == 0:
            return i
    return num


print(reduce_num(101))
