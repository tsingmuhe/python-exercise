#!/usr/bin/env python3

# 输入某年某月某日，判断这一天是这一年的第几天？

class YearError(Exception):
    pass


class MonthError(Exception):
    pass


class DayError(Exception):
    pass


year = int(input('year:\n'))
if year <= 0:
    raise YearError()

month = int(input('month:\n'))
if month <= 0 or month > 12:
    raise MonthError()

day = int(input('day:\n'))
if day <= 0:
    raise DayError()

months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
sumDay = months[month - 1]
sumDay += day

leap = 0
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    leap = 1

if leap == 1 and month > 2:
    sumDay += 1

print("it is the %dth day" % sumDay)
