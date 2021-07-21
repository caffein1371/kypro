N,M,C = map(int,input().split())

Blist = list(map(int,input().split()))
Alist = []
for i in range(N):
  alist = list(map(int,input().split()))
  Alist.append(alist)

#print (Blist)
#print (Alist)
count = [0 for _ in range(N)]

for i in range(N):
  for j in range(M):
    #print ('{} {}'.format(Alist[i][j],Blist[j]))
    count[i]+= Blist[j]*Alist[i][j]
    
for i in range(N):
  count[i]+=C
print (sum([i>0 for i in count]))