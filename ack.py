#!/usr/bin/env python

depth = 0

def ack(m, n):
    global depth
    depth += 1
    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m - 1, 1)
    else:
        return ack(m - 1, ack(m, n - 1))

print ack(3, 3)
print 'depth: %d' % depth
