# ABC151
# 問題文
# 高橋君は N科目のテストを受けます。各テストはK点満点であり、点数はそれぞれ 0以上の整数です。

# 高橋君は N−1科目のテストを既に受けており、i番目の科目のテストの点数はAi点でした。
# 高橋君の目標は、N科目のテストの平均点をM点以上にすることです。
# 高橋君が目標を達成するためには、最後のテストで最低何点取る必要があるか出力してください。
# 達成不可能である場合は、代わりに -1 を出力してください。


N,K,M = map(int,input().split())
Alist = list(map(int,input().split()))

i = 0
temp = 0
flag = False
for i in range(0,K+1):
  mean = (sum(Alist)+i)//N
  if M<=mean:
    temp =i
    flag =True
    break

if flag ==True:
  print (temp)
else :
  print (-1)