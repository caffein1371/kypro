N = int(input())
Alist =list(map(int,input().split()))
Blist =list(map(int,input().split()))
Clist =list(map(int,input().split()))

count = 0
newb = [0 for i in range(N+1)]
for i in range(N):
  newb[Blist[Clist[i]-1]]+=1
#print (newb)
for i in range(N):
  #print ('{} {}'.format(Alist[i],newb[Alist[i]]))
  count+=newb[Alist[i]]
print (count)