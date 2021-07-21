# ABC174
# 問題文
# 2次元平面上に N個の点があります。 i個目の点の座標は (Xi,Yi)です。

# これらのうち、原点からの距離が D以下であるような点は何個ありますか？

# なお、座標 (p,q)にある点と原点の距離は √p2+q2で表されます。
import math

N, D = map(int,input().split())

a = []
n = 0
for i in range(N):
  p,q = map(int, input().split())
  z = math.sqrt(p**2+q**2)
  if z <= D:
    n+=1
    
#print (a)
print (n)