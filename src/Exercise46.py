#!/usr/bin/env python3

"""
求输入数字的平方，如果平方运算后小于 50 则退出。
"""
res = 50

while res >= 50:
    input_value = int(input("请输入数字："))
    res = input_value ** 2
    if res < 50:
        break
    else:
        print("result:%d" % res)
