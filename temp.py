##########################################
import io
import sys

_INPUT = """\
6 5
8 -3 5 7 0 -4




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,K = map(int,input().split())
Alist = list(map(int,input().split()))
ans = 0
tmp = [0 for i in range(N+1)]
for i in range(N):
        tmp[i+1]=tmp[i]+Alist[i]
from collections import defaultdict
mp = defaultdict(int)

for r in range(1,N+1):
        mp[tmp[r-1]]+=1
        ans+=mp[tmp[r]-K]

print (ans)