#!/usr/bin/env python3

"""
请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
"""

weeks = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')


def is_match(day_str, index, target_str):
    if len(day_str) < index + 1:
        return False
    if target_str == day_str[index]:
        return True
    return False


match_arr = list(weeks)
input_arr = []
while True:
    input_arr.append(input("字符："))
    match_arr_tmp = []
    for day in match_arr:
        if is_match(day, len(input_arr) - 1, input_arr[-1]):
            match_arr_tmp.append(day)

    if len(match_arr_tmp) == 1:
        print("matched:%s" % match_arr_tmp[0])
        break
    elif len(match_arr_tmp) == 0:
        print("no match")
        break
    else:
        print(match_arr_tmp)
        match_arr = match_arr_tmp
