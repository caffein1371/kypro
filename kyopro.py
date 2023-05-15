##########################################
import io
import sys

_INPUT = """\
6
ATTATA











"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
S = input()

import collections

c = collections.Counter(S)
if N-c.most_common()[0][1]==c.most_common()[0][1]:
    a = 0
    b = 0
    for i in S:
        if i=='A':
            a+=1
            if a==c.most_common()[0][1]:
                print ('A')
                quit()
        else:
            b+=1
            if b==c.most_common()[0][1]:
                print ('T')
                quit()

else:
    print (c.most_common()[0][0])