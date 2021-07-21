N,X = map(int, input().split())
Alist = list(map(int, input().split()))

Blist = [s for s in Alist if s != X]
#print ( [s for s in Alist if s != X])
#print (Blist)

for i,item in enumerate(Blist):
  if i==len(Blist)-1:
    print (item)
  else:
    print (item,end =' ')