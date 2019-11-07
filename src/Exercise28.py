#!/usr/bin/env python3

"""
有5个人坐在一起，问第五个人多少岁？他说比第4个人大两岁。问第4个人岁数，他说比第3个人大两岁。
问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
"""


def reduce_age(num):
    if num == 1:
        return 10
    else:
        return reduce_age(num - 1) + 2


print(reduce_age(5))
