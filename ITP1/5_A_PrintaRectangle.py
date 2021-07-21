# 長方形の描画
# たてH cm よこ W cm の長方形を描くプログラムを作成して下さい。
# 1 cm × 1cm の長方形を '#'で表します。

while True:
  H,W = map(int,input().split())
  if H ==0 and W==0:
    break
  for i in range(H):
    for j in range(W):
        print ('#',end ='')
    print ('')
  print ('')