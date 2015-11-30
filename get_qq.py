#!/usr/bin/env python

qq = []
with open('8.txt') as f:
    lines = f.readlines()

    for line in lines:
        try:
            qq.append(int(line.strip()))
        except ValueError, e:
            pass
qq.sort()
f = open('qq.txt', 'w')
for num in qq:
    f.write(str(num) + '\n')
f.close()