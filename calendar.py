#!/usr/bin/env python

'''Simple calendar class'''

from operator import add

class Calendar(object):
    def __init__(self, year, month, day):
        super(Calendar, self).__init__()

        self.daysInMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.year = year
        self.month = month
        self.day = day
        self.isLeapYear = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
        if self.isLeapYear:
            self.daysInMonths[1] += 1

    def dayOfYear(self):
        return reduce(add, self.daysInMonths[0:self.month-1]) + self.day

def main():
    c = Calendar(2015, 12, 29)
    print c.dayOfYear()

    c = Calendar(2004, 12, 29)
    print c.dayOfYear()

if __name__ == '__main__':
    main()