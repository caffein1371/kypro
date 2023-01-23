##########################################
import io
import sys

_INPUT = """\
3 1001
1 1
2 1
100 10






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
#個数制限付き部分和問題
N,X = map(int,input().split())

INF = 1<<29
A = []
B = []
for i in range(N):
    a,b = map(int,input().split())
    A.append(a)
    B.append(b)


dp =[[INF for i in range(10011)] for j in range(111)]
dp[0][0]=0

for i in range(N):
    for j in range(X+1):
        #print (i,j)
        if dp[i][j]<INF:
            dp[i+1][j]=0
        if j>=A[i]:
            if dp[i][j-A[i]]<INF:
                dp[i+1][j]=min(dp[i+1][j],1)
            if dp[i+1][j-A[i]]<B[i]:
                dp[i+1][j]=min(dp[i+i][j],dp[i+1][j-A[i]]+1)

if dp[N][X]<INF:
    print ('Yes')
else:
    print ('No')