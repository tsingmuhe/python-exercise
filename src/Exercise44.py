#!/usr/bin/env python3

"""
两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵.
"""
import random

x = [[random.randint(0, 9) for j in range(3)] for i in range(3)]
y = [[random.randint(0, 9) for j in range(3)] for i in range(3)]

print(x)
print(y)

result = []
for i in range(3):
    item = []
    for j in range(3):
        item.append(x[i][j] + y[i][j])
    result.append(item)

print(result)
