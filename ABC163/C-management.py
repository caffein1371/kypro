# 問題文
# N人の社員からなる会社があり、各社員には 1,...,Nの社員番号が割り当てられています。
# 社員番号 1の社員以外の全ての社員には、自分より社員番号が小さい直属の上司がちょうど 1人います。
# Xさんが Yさんの直属の上司であるとき、Yさんは Xさんの直属の部下であるといいます。
# 社員番号 iの社員の直属の上司の社員番号が Aiであることが与えられます。各社員について直属の部下が何人いるか求めてください。

N = int(input())
Alist = list(map(int,input().split()))

anslist = [0]*(N+1)
for i in range(len(Alist)):
  anslist[Alist[i]]+=1
#print (anslist)
for i in range(len(anslist)):
  if i!=0:
    print (anslist[i]) 