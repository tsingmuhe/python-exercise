#!/usr/bin/env python3

"""
将一个数组逆序输出。
"""
import random

param = [random.randint(1, 9) for x in range(0, 10)]

print(param)
param.reverse()
print(param)
