#!/usr/bin/env python3

"""
求一个3*3矩阵主对角线元素之和。
"""
import random

input_arr = [[random.randint(0, 9) for j in range(0, 3)] for i in range(0, 3)]

sum_result = 0
for i in range(3):
    for j in range(3):
        if i == j:
            sum_result += input_arr[i][j]

print(input_arr)
print(sum_result)
