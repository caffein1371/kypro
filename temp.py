##########################################
import io
import sys

_INPUT = """\
7 3
2 0 2 3 2 1 9







"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,K = map(int,input().split())
Alist = list(map(int,input().split()))
Alist = sorted(set(Alist))
ans = -1

import itertools
flag = False
for i in range(len(Alist)):
    if i!=Alist[i]:
        print (i-1)
        quit()