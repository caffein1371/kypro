##########################################
import io
import sys

_INPUT = """\
4
0 1 3 8




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())

import math

Alist = list(map(int,input().split()))
n =0
for i in range(len(Alist)):
    if Alist[i]!=0:
        n+=1

#print (sum(Alist)/n)
print(math.ceil(sum(Alist)/n))