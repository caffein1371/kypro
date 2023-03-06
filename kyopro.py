##########################################
import io
import sys

_INPUT = """\
hello
3




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
s= input()
k = int(input())

import itertools
ans = 0
if len(s)<k:
    print (ans)
    quit()
temp = []
for i in range(0,len(s)-k):
    temp.append(s[i:i+k])
ans = len(set(temp))
print (ans)