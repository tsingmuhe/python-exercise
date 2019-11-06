#!/usr/bin/env python3

"""
两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。
已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
"""
ad = ('y', 'z')
bd = ('x', 'y', 'z')
cd = ('y')

for a2 in ad:
    for b2 in bd:
        for c2 in cd:
            if a2 != b2 and a2 != c2 and b2 != c2:
                print('order is a -- %s\t b -- %s\tc--%s' % (a2, b2, c2))
