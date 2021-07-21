# ABC156
# 問題文
# 数直線上にN人の人が住んでいます。
# i番目の人が住んでいるのは座標 Xiです。
# あなたは N人全員が参加する集会を開くことを考えています。
# 集会は数直線上の任意の 整数値の座標 で開くことができ、座標 
# Pで集会を開くとき、i番目の人は集会に参加するために(Xi−P)2の体力を消費します。
# N
#  人が消費する体力の総和としてありえる値の最小値を求めてください。

import math
N = int(input())
Xlist = list(map(int,input().split()))

min =10**5
meandown = math.floor(sum(Xlist)/N)
meanup = math.ceil(sum(Xlist)/N)
sumdown=0
sumup = 0
for i in range(len(Xlist)):
  sumdown+= (Xlist[i]-meandown)**2
  sumup+= (Xlist[i]-meanup)**2
  
if sumdown<sumup:
  print(sumdown)
else:
  print (sumup)