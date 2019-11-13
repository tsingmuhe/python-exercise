#!/usr/bin/env python3

"""
对10个数进行排序。
"""
import random


def bubblesort(param_arr):
    end = len(param_arr)
    for j in range(0, end - 1):
        for k in range(j + 1, end):
            if param_arr[j] > param_arr[k]:
                param_arr[j], param_arr[k] = param_arr[k], param_arr[j]
    return param_arr


input_arr = [random.randint(0, 9) for i in range(0, 10)]
print("排序前: %s" % input_arr)
print("排序后: %s" % bubblesort(input_arr))
