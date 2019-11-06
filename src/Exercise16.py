#!/usr/bin/env python3

"""
输出指定格式的日期。
"""
import datetime

print(datetime.date.today().strftime('%d/%m/%Y'))

birth = datetime.date(1989, 10, 2)
print(birth.strftime('%d/%m/%Y'))

birth = birth + datetime.timedelta(days=1)
print(birth.strftime('%d/%m/%Y'))
