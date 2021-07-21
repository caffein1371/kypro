# ABC165
# 問題文
# ジャンボ高橋君はゴルフの練習をすることにしました。
# ジャンボ高橋君の目標は飛距離をKの倍数にすることですが、ジャンボ高橋君の出せる飛距離の範囲は A以上 B以下です。
# 目標の達成が可能であれば OK と、不可能であれば NG と出力してください。

K = int(input())
A,B = map(int,input().split())

amari =int(B/K)
if A<=K*amari and K*amari<=B:
  print('OK')
else :
  print('NG')