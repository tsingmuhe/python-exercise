#!/usr/bin/env python3

"""
一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
"""
from functools import reduce

h = int(input("输入高度:"))
num = int(input("反弹次数:"))

h_arr = [h]

for i in range(0, num - 1):
    tmp = h_arr[i * 2] / 2
    h_arr.append(tmp)
    h_arr.append(tmp)

print(reduce(lambda x, y: x + y, h_arr))
print(h_arr[-1] / 2)
