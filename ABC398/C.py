##########################################
import io
import sys

_INPUT = """\
4
10 10 9 6


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))
from collections import defaultdict
d = defaultdict(list)
#print (d)

for i in range(0,len(Alist)):
    d[Alist[i]].append(i)

temp = -1
ans = -1
for i in reversed(Alist):
    if len(d[i])==1:
        if i>temp:
            temp = i
            ans = d[i][0]+1


print (ans)
