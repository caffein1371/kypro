# ABC165
# 問題文
# 高橋くんはAtCoder銀行に 100円を預けています。
# AtCoder銀行では、毎年預金額の 
# 1% の利子がつきます(複利、小数点以下切り捨て)。
# 利子以外の要因で預金額が変化することはないと仮定したとき、高橋くんの預金額が初めてX円以上になるのは何年後でしょうか。

import math
X =int(input())

# math.floorではなく//を使用する
#https://takeg.hatenadiary.jp/entry/2019/09/01/110530
# math.floorは桁が大きくなるとfloatに勝手に変換し，誤差が生じる

deposit = 100
year = 0
while deposit<X:
  deposit = deposit+int(deposit/100)
  #print(deposit)
  year+=1
  
print (year)