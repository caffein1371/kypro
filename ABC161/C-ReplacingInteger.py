# ABC161
# 問題文
# 青木君は任意の整数 xに対し、以下の操作を行うことができます。
# 操作:xを xと Kの差の絶対値で置き換える。
# 整数 Nの初期値が与えられます。この整数に上記の操作を 0回以上好きな回数行った時にとりうる Nの最小値を求めてください。

N,K = map(int,input().split())
 
min = N%K
if min>abs(min-K):
  min = abs(min-K)
 
print (min)