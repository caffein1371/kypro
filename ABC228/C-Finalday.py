N,K = map(int,input().split())
plist =[]
for i in range(N):
  p1,p2,p3 = map(int,input().split())
  plist.append(p1+p2+p3)
p2list = sorted(plist)
tempmax =p2list[-K]
#print (tempmax)
for i in range(N):
  if plist[i]+300>=tempmax:
    print ("Yes")
  else:
    print ("No")