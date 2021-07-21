H,W = map(int,input().split())
 
Alist = []
minnum = 100
for i in range(H):
  temp = list(map(int,input().split()))
  Alist.append(temp)
  if minnum>min(temp):
    minnum = min(temp)
 
ans = 0
for i in range(H):
  for j in range(W):
    ans+= abs(Alist[i][j]-minnum)
print (ans)