#!/usr/bin/env python

units = {'dollar':100, 'dollars':100, 'quarter':25, 'quarters':25,
'dime':10, 'dimes':10,'nickel':5, 'nickels':5, 'penny':1, 'pennies':1,
'cent':1, 'cents':1}

while 1:
    while 1:
        try:
            m = raw_input('Enter some money: ').split()
            unit = units[m[1]]
            money = float(m[0])
            del m
        except ValueError:
            print 'Not valid! Try again'
            continue
        except KeyError:
            print 'unit not supported, try again'
            continue
        break

    cents = int(money * unit)
    cnt = 0

    for i in range(cents / 25):
        remain1 = cents - i *  25
        for j in range(remain1 / 10):
            remain2 = remain1 - j * 10
            for k in range(remain2 / 5):
                l = remain2 - k * 5
                cnt += 1
                print ('%d:' % cnt), i, 'quarters,' if i > 1 else 'quarter,',\
                j, 'dimes,' if j > 1 else 'dime,',\
                k, 'nickels,' if k > 1 else 'nickel,',\
                l, 'pennies.' if l > 1 else 'penny.'

    if raw_input('Continue? ')[0].lower() != 'y':
        break