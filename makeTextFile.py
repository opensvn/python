#!/usr/bin/env python

'''simple script for generating text file from user's input'''

import os

while 1:
    filename = raw_input('Enter a filename: ')
    if not filename or os.path.exists(filename):
        print 'empty filename or file already exists'
        continue
    break

all = []

while 1:
    line = raw_input('Enter a line of text: ')
    if line == '.':
        break
    all.append(line)

fobj = open(filename, 'w')
fobj.write('\n'.join(all))
fobj.close()