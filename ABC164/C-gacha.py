# ABC164
# 問題文
# くじ引きを N回行い、i回目には種類が文字列 Siで表される景品を手に入れました。
# 何種類の景品を手に入れましたか？

N = int(input())

slist = []
for i in range(N):
  slist.append(input())
print (len(set(slist)))