#!/usr/bin/env python3

"""
有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
"""

i = 1
j = 2

total = 0

for k in range(0, 20):
    total = total + (j / i)
    i, j = j, i + j

print(total)
