#!/usr/bin/env python3

# 暂停一秒输出，并格式化当前时间。
import time

for i in range(10):
    print(time.strftime("%Y%m%d %H:%M:%S"))
    time.sleep(1)
