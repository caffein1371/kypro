# ABC164
# 問題文
# 羊が S匹、狼が W匹います。
# 狼の数が羊の数以上のとき、羊は狼に襲われてしまいます。
# 羊が狼に襲われるなら unsafe、襲われないなら safe を出力してください。

S,W = map(int,input().split())

if S>W:
  print ('safe')
else :
  print ('unsafe')