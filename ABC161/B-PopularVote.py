# ABC161
# 問題文
# N種類の商品に対して人気投票を行いました。商品 iは Ai票を得ています。
# この中から人気商品 M個を選びます。ただし、得票数が総投票数の 1/4M未満であるような商品は選べません。
# 人気商品 M個を選べるなら Yes、選べないなら No を出力してください。

N,M = map(int,input().split())

Alist = list(map(int,input().split()))

Alist = sorted(Alist,reverse=True)
#print (sum(Alist))
Ans = "No"
for i in range(M):
  #print (Alist[i])
  #print((sum(Alist)/4*M))
  if Alist[i]>=(sum(Alist)/(4*M)):
    Ans ="Yes"
  else:
    Ans = "No"
    
print (Ans)