##########################################
import io
import sys

_INPUT = """\
45


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
dp = [0 for i in range(N+1)]
dp[0]=1
dp[1]=1
for i in range(2,N+1):
    dp[i]=dp[i-1]+dp[i-2]
print (dp[-1])