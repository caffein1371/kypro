##########################################
import io
import sys

_INPUT = """\
4



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
mod = 998244353

dp =[[0 for i in range(11)] for j in range(N+1)]
print (dp)
for i in range(1,10):
    dp[1][i]=1

for d in range(2,N+1):
    for i in range(1,10):
        for j in range(max(1,i-1),min(10,i+1)):
            print (d,i)
            print (d,j)
            dp[d][j]+=dp[d-1][i]
            dp[d][j]%=mod

print (dp)
ans = 0
for i in range(1,10):
    ans+=dp[N][i]
    ans%=mod

print (ans)