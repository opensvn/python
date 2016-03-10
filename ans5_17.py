#!/usr/bin/env python

'''Generate a list of a random number(1 < N <= 100)
of random numbers (0 <= n <= 2 ** 31 -1).Then randomly
select a set of these numbers (1 <= N <= 100),
sort them, and display this subset.'''

from random import randint

def random_of_randoms():
    max_number = 2 ** 31
    number = randint(2, 100)
    return [randint(0, max_number) for i in range(number)]

def select_part(l):
    length = len(l)

    c = [x for x in range(length)]
    number = randint(2, length)

    i = 0
    while i < number:
        n = randint(0, length - 1)
        if n > i:
            c[i], c[n] = c[n], c[i]
            i += 1
        elif n == i:
            i += 1

    selected = []
    for i in range(number):
        selected.append(l[c[i]])

    return selected

def main():
    numbers = random_of_randoms()
    selected = select_part(numbers)

    print 'all numbers:'
    print numbers

    print 'selected numbers:'
    print selected

    print 'sorted:'
    print sorted(selected)

if __name__ == '__main__':
    main()
