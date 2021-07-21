# フレームの描画
# 以下のような、たてH cm よこ W cm の枠を描くプログラムを作成して下さい。
# ##########
# #........#
# #........#
# #........#
# #........#
# ##########
# 上図は、たて 6 cm よこ 10 cm の枠を表しています。

while True:
  H,W = map(int,input().split())
  if H ==0 and W==0:
    break
  for i in range(H):
    for j in range(W):
        if i ==0 or i==H-1 or j==0 or j==W-1:
            print ('#',end ='')
        else :
            print ('.',end ='')
    print ('')
  print ('')