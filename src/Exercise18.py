#!/usr/bin/env python3

"""
求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
"""

# 1
# a = int(input("a:"))
# n = int(input("n:"))
#
# total = 0
# for i in range(1, n + 1):
#     total += int('1' * i) * a
#
# print(total)
from functools import reduce

a = int(input("a:"))
n = int(input("n:"))

arr = [0]

for i in range(0, n):
    arr.append(arr[i] * 10 + a)

print(reduce(lambda x, y: x + y, arr))
