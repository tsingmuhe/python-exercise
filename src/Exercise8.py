#!/usr/bin/env python3

# 输出 9*9 乘法口诀表。

for i in range(1, 10):
    if i > 1:
        print()
    for j in range(1, i + 1):
        print("%d*%d=%d" % (i, j, i * j), end=' ')
