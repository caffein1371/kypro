##########################################
import io
import sys

_INPUT = """\
15
1 900000000
0 600000000
1 -300000000
0 -700000000
1 200000000
1 300000000
0 -600000000
1 -900000000
1 600000000
1 -100000000
1 -400000000
0 900000000
0 200000000
1 -500000000
1 900000000


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())

DP = [[-float('INF')]*2 for i in range(N+1)]
DP[0][0]=0
#print (DP)
x = []
y = []
for i in range(N):
    X,Y = map(int,input().split())
    x.append(X)
    y.append(Y)

for i in range(N):
    #何も食べない時
    DP[i+1][0] = max(DP[i+1][0],DP[i][0])
    DP[i+1][1] = max(DP[i+1][1],DP[i][1])

    #解毒剤を飲む時
    if x[i]==0:
        #毒を飲んでない状態から解毒
        DP[i+1][0]=max(DP[i+1][0],DP[i][0]+y[i])
        #毒を飲んでいる状態から解毒
        DP[i+1][0]=max(DP[i+1][0],DP[i][1]+y[i])
    else:
        #毒を飲んでいない状態から解毒
        DP[i+1][1]=max(DP[i][0]+y[i],DP[i+1][1])

print (max(DP[N][1],DP[N][0]))