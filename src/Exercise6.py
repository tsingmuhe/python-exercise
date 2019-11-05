#!/usr/bin/env python3

# 斐波那契数列。

num = int(input("需要的斐波那契数量："))

if num < 0:
    raise Exception()

arr = [0, 1]
for i in range(1, num):
    arr.append(arr[i - 1] + arr[i])

print(arr)
