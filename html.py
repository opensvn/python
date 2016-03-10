#!/usr/bin/env python

s = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""
t = ''

for c in s:
    # if c == 'k':
    #     t += 'm'
    # elif c == 'o':
    #     t += 'q'
    # elif c == 'e':
    #     t += 'g'
    # else:
    #     t += c
    if c == 'm':
        t += 'k'
    elif c == 'q':
        t += 'o'
    elif c == 'g':
        t += 'e'
    else:
        t += c
print t