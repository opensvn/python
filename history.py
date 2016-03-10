#!/usr/bin/env python

import sys

def main():
    if len(sys.argv) != 2:
        print 'argument error'
        return

    fname = sys.argv[1]

    with open(fname) as f:
        cmd = set()
        for line in f:
            cmd.add(line.rstrip())

    for i in cmd:
        print i

if __name__ == '__main__':
    main()