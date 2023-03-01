##########################################
import io
import sys

_INPUT = """\
8 3
2 6 8
-17683 17993
93038 47074
58079 -57520
-41515 -89802
-72739 68805
24324 -73073
71049 72103
47863 19268






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,K = map(int,input().split())
Alist = list(map(int,input().split()))
XY = []

for i in range(N):
        x,y = map(int,input().split())
        XY.append([x,y])
#print (XY)
import math
ans = 0
#全員とあかりを持っている人の距離の最小を計算し，
#その中からmaxを取ることによって全員をカバーするための値を算出する
for i in range(N):
        temp = float('inf')
        for j in range(len(Alist)):
                temp = min(temp,math.sqrt((XY[i][0]-XY[Alist[j]-1][0])*(XY[i][0]-XY[Alist[j]-1][0])+(XY[i][1]-XY[Alist[j]-1][1])*(XY[i][1]-XY[Alist[j]-1][1])))
        ans = max(temp,ans)
print (float(ans))
                        
