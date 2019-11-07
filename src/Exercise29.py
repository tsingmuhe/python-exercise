#!/usr/bin/env python3

"""
给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
"""

total = 0


def reduce_num(num):
    global total
    if num < 10:
        total += 1
        return str(num)
    else:
        total += 1
        return str(num % 10) + reduce_num(num // 10)


print(reduce_num(1234512312))
print(total)
