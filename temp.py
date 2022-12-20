##########################################
import io
import sys

_INPUT = """\
10






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
ans = [[1 for i in range(j)]for j in range(1,N+1)]

for i in range(0,N):
    for j in range(i):
        if i==j or j==0:
            pass
        else:
            ans[i][j]=ans[i-1][j-1]+ans[i-1][j]
    print (*ans[i])
         