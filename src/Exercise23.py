#!/usr/bin/env python3

"""
打印出如下图案（菱形）:
   *
  ***
 *****
*******
 *****
  ***
   *
"""

c = 11

middle = (c + 1) / 2 - 1

for y in range(0, c):
    for x in range(0, c):
        if y <= middle:
            if middle - y <= x <= middle + y:
                print('*', end='')
            else:
                print(' ', end='')
        else:
            if x < y - middle or x > c - y + middle - 1:
                print(' ', end='')
            else:
                print('*', end='')
    print('')
