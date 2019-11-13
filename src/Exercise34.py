#!/usr/bin/env python3

"""
练习函数调用。
"""


def hello_world():
    print('hello world')


def three_hellos():
    for i in range(3):
        hello_world()


print(__name__)
if __name__ == '__main__':
    print(__name__)
    three_hellos()
