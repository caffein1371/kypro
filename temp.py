##########################################
import io
import sys

_INPUT = """\
100 5
1
23
45
67
89




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,K = map(int,input().split())
Alist = list(map(int,input().split()))

ans = 1
for i in range(K):
    ans*=Alist[i]
for i in range(K,N):
    
    

