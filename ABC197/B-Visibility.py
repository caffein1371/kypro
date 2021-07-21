H,W,X,Y = map(int,input().split())
templist = []
tatelist = []
for i in range(H):
  a=input()
  templist.append(a)
  tatelist.append(a[X-1])
count =-3
#X前から
for i in range(X-1,W):
  print (templist[Y-1][i])
  if templist[Y-1][i]=='.':
    count +=1
  elif templist[Y-1][i]=='#':
    break
print (count)
for i in range(X-1,-1,-1):
  print (templist[Y-1][i])
  if templist[Y-1][i]=='.':
    count +=1
  elif templist[Y-1][i]=='#':
    break
print (count)

tate = ''.join(tatelist)
print (tate)
for i in range(Y-1,H):
  print (tate[i])
  if tate[i]=='.':
    count +=1
  elif tate[i]=='#':
    break
print (count)
for i in range(Y-1,-1,-1):
  print (tate[i])
  if tate[i]=='.':
    count +=1
  elif tate[i]=='#':
    break
print (count)
  
    
print (count)
#print (templist[Y-1][0:X-1])
#X後ろから
#print (templist[Y-1][X:])
#print (''.join(tatelist[0:X-1]).count('.'))
#print (''.join(tatelist[X:]).count('.'))
