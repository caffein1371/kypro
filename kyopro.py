##########################################
import io
import sys

_INPUT = """\
3 3
3 2 2
2 1 3
1 5 4




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
H,W = map(int,input().split())
A = []
ans = 0
for i in range(H):
    Alist = list(map(int,input().split()))
    A.append(Alist)
DP = [[False for i in range(W)]for j in range(H)]
DP[0][0]=True
print (DP)
temp = []
temp.append(A[0][0])
print (temp)
for i in range(H):
    for j in range(W):
        if i+1<H and A[i+1][j]!=A[i][j] and DP[i][j]==True and A[i+1][j] not in temp:
            DP[i+1][j]=True
            temp.append(A[i+1][j])
        elif i+1<H:
            DP[i+1][j]=False
        if j+1<W and A[i][j+1]!=A[i][j] and DP[i][j]==True and A[i][j+1] not in temp:
            DP[i][j+1]=True
            temp.append(A[i][j+1])
        elif j+1<W:
            DP[i][j+1]=False
        if i==H-1 and j==W-1 and DP[i][j]==True:
            ans+=1
print (ans)