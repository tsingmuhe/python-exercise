#!/usr/bin/env python3

"""
有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
"""
import random


def bubblesort(param_arr):
    end = len(param_arr)
    for j in range(0, end - 1):
        for k in range(j + 1, end):
            if param_arr[j] > param_arr[k]:
                param_arr[j], param_arr[k] = param_arr[k], param_arr[j]
    return param_arr


input_arr = bubblesort([random.randint(0, 9) for i in range(0, 10)])

print(input_arr)
insert_value = int(input("num:"))
len_origin = len(input_arr)

for i in range(0, len_origin - 1):
    if input_arr[i] != input_arr[i + 1] and (input_arr[i] - insert_value) * (input_arr[i + 1] - insert_value) <= 0:
        input_arr.insert(i + 1, insert_value)
        break

if len_origin == len(input_arr):
    input_arr.append(insert_value)

print(input_arr)
