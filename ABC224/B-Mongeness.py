H,W = map(int,input().split())
Alist  = []
for i in range(H):
  alist = list(map(int,input().split()))
  Alist.append(alist)
#print (Alist)
 
for i in range(H):
  for k in range(i,H):
    for j in range(W):
      for l in range(j,W):
        if Alist[i][j]+Alist[k][l]>Alist[k][j]+Alist[i][l]:
          print ("No")
          quit()
print ("Yes")