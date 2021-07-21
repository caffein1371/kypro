H,W = map(int,input().split())
#https://www.sejuku.net/blog/67215
numberlist =[[0 for i in range(W)] for j in range(H)]

#print (numberlist)
Slist =[]
for i in range(H):
  Slist.append(list(input()))

#print (Slist)
for i in range(H):
  #print (len(Slist[i]))
  #print (len(numberlist[i]))
  for j in range(W):
    #print (len(Slist[i][j]))
    #print (len(numberlist[i][j]))
    if Slist[i][j]=='#':
      #print (numberlist[i][j])
      for k in range(-1,2):
        for l in range(-1,2):
          if i+k>=0 and i+k<H and j+l>=0 and j+l<W:
            #print ('i+k={}'.format(i+k))
            #print ('j+l={}'.format(j+l))
            if numberlist[i+k][j+l] != '#':
              numberlist[i+k][j+l]+=1
      numberlist[i][j] = '#'
#print (numberlist)
for i in range(H):
  for j in range(W):
    if j==W-1:
      print (numberlist[i][j])
    else:
      print (numberlist[i][j],end='')