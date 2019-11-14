#!/usr/bin/env python3

"""
输出一个随机数。
"""
import random

print(random.random())  # 输入0-1之间的随机数
print(random.uniform(10, 20))  # 输出10-20之间的随机数
print(random.randint(10, 20))  # 输出10-20之间的随机整数
print(random.choice([x for x in range(1, 100)]))  # 输出1-99间的随机数
