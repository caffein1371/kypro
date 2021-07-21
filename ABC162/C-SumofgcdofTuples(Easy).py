# ABC162
# 問題文
# K∑a=1K∑b=1K∑c=1
# gcd(a,b,c)を求めてください。
# ただし、gcd(a,b,c)はa,b,cの最大公約数を表します。

import math

K = int(input())

sum = 0
for i in range(1,K+1):
  for j in range(1,K+1):
    temp = math.gcd(i,j)
    for k in range(1,K+1):
      sum+=math.gcd(temp,k)
print (sum)
