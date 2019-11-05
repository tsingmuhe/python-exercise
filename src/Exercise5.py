#!/usr/bin/env python3

# 输入三个整数x,y,z，请把这三个数由小到大输出。

n1 = int(input("num 1:\n"))
n2 = int(input("num 2:\n"))
n3 = int(input("num 3:\n"))

arr = [n1, n2, n3]
arr.sort()

print(arr)
