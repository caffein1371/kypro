# ABC168
# 問題文
# 英小文字からなる文字列 Sがあります。
# Sの長さが K以下であれば、Sをそのまま出力してください。
# Sの長さが Kを上回っているならば、先頭 K文字だけを切り出し、末尾に ... を付加して出力してください。

K = int(input())
S = input()

if len(S) <=K:
  print (S)
else :
  print(S[:K]+"...")