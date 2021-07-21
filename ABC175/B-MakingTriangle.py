
#ABC175
# 問題文
# 1,⋯,Nの番号がついたN本の棒があります。棒 i(1≤i≤N)の長さは Liです。
# このうち、三角形を作ることのできるような長さの異なる 
# 3本の棒を選ぶ方法は何通りあるでしょうか。
# つまり、3つの整数 1≤i<j<k≤Nの組であって次の2つの条件の両方を満たすものの個数を求めてください。
N = int(input())
Llist = list(map(int,input().split()))

n =0
#print(Llist)
for i in range(N-2):
  for j in range(N-1):
    for k in range(N):
      if i<j and j<k and Llist[i]!=Llist[j] and Llist[j]!=Llist[k] and Llist[i]!=Llist[k] and Llist[i]+Llist[j]>Llist[k] and Llist[j]+Llist[k]>Llist[i] and Llist[i]+Llist[k]>Llist[j]:
        #print ('{}{}{}'.format(Llist[i], Llist[j], Llist[k]))
        #print ('{}{}{}'.format(i, j, k))
        n+=1
print(n)