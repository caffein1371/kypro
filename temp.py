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
N,M = map(int,input().split())
A = []
mod = 1000000007

A = [True for i in range(N+3)]
for i in range(M):
    a = int(input())
    A[a]=False

dp=[0 for i in range(N+3)]
dp[0]=1
for n in range(0,N):
    if A[n+1]==True:
        dp[n+1]+=dp[n]
    if A[n+2]==True:
        dp[n+2]+=dp[n]
print (dp[N]%mod)
