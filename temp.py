##########################################
import io
import sys

_INPUT = """\
10
2 2 4 1 1 1 4 2 2 1




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))
from collections import deque

d = deque()
ans = 0
for i in range(N):
        for j in range(Alist[i]):
                if j==0:
                        d.append(1)
                else:
                        d.append(0)
        #print (d)
        while len(d)>3:
                temp = d.popleft()
                if temp==1:
                        ans+=1
print (ans)




