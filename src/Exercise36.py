#!/usr/bin/env python3

"""
求100之内的素数。
"""
from math import sqrt


def is_sushu(num):
    end = int(sqrt(num + 1))

    for i in range(2, end + 1):
        if num % i == 0:
            return False

    return True


print(",".join(str(i) for i in range(2, 100) if is_sushu(i)))
