#!/usr/bin/env python
#-*- coding:utf-8 -*-

class Prime(object):
    '''Calc all the prime numbers less than n.'''

    def __init__(self, n):
        self._top = n
        if self._top < 2:
            self._primes = []
        else:
            self._primes = [2]

        self._find_prime()

    def _find_prime(self):
        for i in xrange(3, self._top, 2):
            for j in self._primes:
                if i % j == 0:
                    break;
            else:
                self._primes.append(i)

    def __str__(self):
        return str(self._primes)

def main():
    p = Prime(1000)
    print p

if __name__ == '__main__':
    main()
