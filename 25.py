#!/usr/bin/env python

def main():
    a = 1
    b = 1

    i = 2
    while len(str(b)) < 1000:
        a, b = b, a + b
        i += 1

    print i
    print b

if __name__ == '__main__':
    main()