#!/usr/bin/env python

'''simple script to read contents of a text file'''

try:
    filename = raw_input('Enter a filename: ')
    fobj = open(filename)
except IOError, e:
    print '%s' % str(e)
else:
    for line in fobj:
        print line,
    fobj.close()