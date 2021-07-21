# AB167
# 問題文
# 1が書かれたカードが A枚、0が書かれたカードが B枚、 −1が書かれたカードが C枚あります。
# これらのカードから、ちょうど K枚を選んで取るとき、取ったカードに書かれた数の和として、 ありうる値の最大値はいくつですか。

A,B,C,K = map(int,input().split())

koa = 0
if A<K:
  koa = A
else :
  koa = K
kob = 0
if B<K-koa:
  kob = B
else :
  kob = K-koa
#print (koa)
#print (kob)
sum = koa+0*kob+(K-(koa+kob))*-1
print (sum)