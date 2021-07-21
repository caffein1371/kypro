# ABC155
# 問題文
# 3つ組の数について、ある2つが等しく、残りの1つがそれらと異なるとき、その3つ組を「かわいそう」であるといいます。
# 3つの整数A,B,Cが与えられるので、この3つ組がかわいそうであれば Yes を、そうでなければ No を出力してください。

A,B,C = map(int,input().split())

if A==B and B==C and A==C:
  print ("No")
elif A!=B and B!=C and A!=C:
  print ("No")
else :
  print ("Yes")