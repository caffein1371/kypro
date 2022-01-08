N,X = map(int,input().split())
Alist = list(map(int,input().split()))
Blist = [False]*len(Alist)
Alist.insert(0,X)
ans= 0
i = 0
while True:
  if Blist[Alist[i]-1]==True:
    break
  else:
    Blist[Alist[i]-1]=True
    i=Alist[i]
    ans+=1
print (ans)