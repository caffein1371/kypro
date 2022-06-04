N,K= map(int,input().split())
Alist = list(map(int,input().split()))
Blist = list(map(int,input().split()))
temp = max(Alist)
for i in range(len(Blist)):
  if temp ==Alist[Blist[i]-1]:
    print ("Yes")
    quit()
print ("No")