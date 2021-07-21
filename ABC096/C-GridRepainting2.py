H,W = map(int,input().split())
mapping = []
for i in range(H):
  mapping.append(input())  
#print (mapping)
tansakux = [0,1,0,-1]
tansakuy = [1,0,-1,0]
for i in range(H):
  for j in range(W):
    if mapping[i][j]=='#':
      count = 0
      for k in range(0,4):
        #print ('{} {}'.format((i+tansakuy[k]),(j+tansakux[k])))
        if (i+tansakuy[k])<0 or (i+tansakuy[k])>=H or (j+tansakux[k])<0 or (j+tansakux[k])>=W:
          continue
        if mapping[i+tansakuy[k]][j+tansakux[k]]=='#':
          count +=1
      if count ==0:
        print ('No')
        quit()
print ('Yes')