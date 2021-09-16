N,X = map(int,input().split())
Alist = list(map(int,input().split()))
Blist = [Alist[i]-1 if i%2==1 else Alist[i] for i in range(len(Alist))]
if sum(Blist)<=X:
  print ("Yes")
else:
  print ("No")