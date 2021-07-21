# チェスボードの描画
# 以下のような、たてH cm よこ W cm のチェック柄の長方形を描くプログラムを作成して下さい。
# #.#.#.#.#.
# .#.#.#.#.#
# #.#.#.#.#.
# .#.#.#.#.#
# #.#.#.#.#.
# .#.#.#.#.#
# 上図は、たて 6 cm よこ 10 cm の長方形を表しています。
# 長方形の左上が "#" となるように描いて下さい。

while True:
  H,W = map(int,input().split())
  if H ==0 and W==0:
    break
  for i in range(H):
    for j in range(W):
      if i%2==0:
        if j%2==0:
          print ('#',end ='')
        else:
          print ('.',end ='')
      elif i%2==1:
        if j%2==0:
          print ('.',end ='')
        else :
          print ('#',end ='')
    print ('')
  print ('')