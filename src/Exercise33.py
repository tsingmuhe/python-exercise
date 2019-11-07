#!/usr/bin/env python3

"""
按逗号分隔列表。
"""

weeks = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

result = ','.join(str(item) for item in weeks)

print(result)
