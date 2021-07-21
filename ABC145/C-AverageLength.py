# ABC145
# 問題文
# 座標平面上に N個の町があります。町 iは、座標 ( xi, yi) に位置しています。町 iと町 jの間の距離は √(xi−xj)2+(yi−yj)2です。
# これらの町を全て 1回ずつ訪れるとき、町を訪れる経路は全部でN!通りあります。1番目に訪れる町から出発し、2番目に訪れる町、3番目に訪れる町、…、を経由し、N番目に訪れる町に到着するまでの移動距離 (町から町への移動は直線移動とします) を、その経路の長さとします。これらの N!通りの経路の長さの平均値を計算してください。

import itertools
import math

N= int(input())
place =[]
for i in range(N):
  placelist = list(map(int,input().split()))
  place.append(placelist)
  
ans = 0
count =0
for i in itertools.permutations(place, r=N):
  for j in range(0,N-1):
    ans+= math.sqrt(((i[j][0]-i[j+1][0])*(i[j][0]-i[j+1][0])+(i[j][1]-i[j+1][1])*(i[j][1]-i[j+1][1])))
  count+=1
  
print (ans/count)