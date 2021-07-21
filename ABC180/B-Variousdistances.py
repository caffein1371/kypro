# ABC180
# 問題文
# N次元空間内の点(x1,…,xN)が与えられます。
# 原点からこの点までの、マンハッタン距離、ユークリッド距離、チェビシェフ距離をそれぞれ求めてください。 ただし、それぞれの距離は次のように計算されます。

import math
import numpy as np
N = int(input())
xlist = list(map(int,input().split()))

#マンハッタン距離
ans = 0
ansU = 0
anslist =[]
for i in range(N):
  ans+=abs(xlist[i])
  ansU+=(xlist[i])*(xlist[i])
  anslist.append(abs(xlist[i]))
print (ans)
#ユークリッド距離
print (np.sqrt(ansU))
#チェビシェフ距離
print (max(anslist))