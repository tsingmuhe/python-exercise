#!/usr/bin/env python3

"""
计算字符串长度。　
"""
current_line = [1]
next_line = []
for i in range(0, 10):
    print(current_line)
    for j in range(len(current_line) - 1):
        next_line.append(current_line[j] + current_line[j + 1])
    next_line.insert(0,1)
    next_line.append(1)

    current_line = next_line
    next_line=[]
