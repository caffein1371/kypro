##########################################
import io
import sys

_INPUT = """\
217




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
X = int(input())
bag = [100,101,102,103,104,105]

dp = [False for i in range(10**5+1000)]
dp[0]=True

for i in range(X):
        if dp[i]:
                for j in range(6):
                        dp[i+j+100]=True

if dp[X]:
        print (1)
else:
        print (0)
