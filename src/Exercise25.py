#!/usr/bin/env python3

"""
求1+2!+3!+...+20!的和。
"""

total = 0
tmp = 1
for i in range(1, 21):
    tmp = tmp * i
    total += tmp

print(total)
