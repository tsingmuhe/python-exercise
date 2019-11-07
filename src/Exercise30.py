#!/usr/bin/env python3

"""
一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
"""


def cal(num):
    num_str = str(num)
    num_str_len = len(num_str)
    num_str_len_middle = num_str_len // 2

    for i in range(0, num_str_len_middle):
        if num_str[i] != num_str[- i - 1]:
            return False

    return True


print(cal(int(input("num:"))))
