# ABC176
# 問題文
# N人が1列に並んでおり、前から i番目の人の身長は Aiです。

# それぞれの人の足元に、高さが 
# 0以上の踏み台を設置し、全ての人が次の条件を満たすようにしたいです。
# 条件：踏み台を込めて身長を比較したとき、自分より前に、自分より背の高い人が存在しない
# この条件を満たす時の、踏み台の高さの合計の最小値を求めてください。

N = int(input())
Alist = list(map(int,input().split()))

dailist = [0]*N
Alist.append(0)
dailist.append(0)
max = 0
for i in range(N):
  if Alist[i]>max:
    max=Alist[i]
    #dailist[i+1]=max-Alist[i+1]
    #print("max="+str(max))
  
  if max>Alist[i+1]:
    dailist[i+1]=max-Alist[i+1]
    #print ("dailist="+str(dailist[i+1]))

#print (Alist)
#print (dailist)
del dailist[-1]
print (sum(dailist))
