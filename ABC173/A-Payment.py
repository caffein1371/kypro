# ABC173
# 問題文
# お店で N円の商品を買います。

# 1000円札のみを使って支払いを行う時、お釣りはいくらになりますか？

# ただし、必要最小限の枚数の 
# 1000円札で支払いを行うものとします。

X = int(input())

i = 0
x = 0
while x<X:
  x = i*1000
  i+=1
print (x-X)