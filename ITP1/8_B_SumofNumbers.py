# 数字の和
# 与えられた数の各桁の和を計算するプログラムを作成して下さい

while True:
  x = input()
  if x=="0":
    break
  sum = 0
  for i in range(len(x)):
    sum+=int(x[i])
  print (sum)