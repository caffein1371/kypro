# ABC154
# 問題文
# 整数列 A1,A2,...,ANが与えられます。 この整数列のどの2つの要素も互いに異なるならば YES を、そうでないなら NO を出力してください。

N = int(input())
Alist = list(map(int,input().split()))

temp = len(Alist)
ansnum = len(list(set(Alist)))

if ansnum == temp:
  print ("YES")
else :
  print ("NO")