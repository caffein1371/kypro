S = input()
if S.count('o')>4:
  print (0)
  quit()

marulist = []
hatenalist =[]
batsulist = []
for i in range(len(S)):
  if S[i]=='o':
    marulist.append(i)
  elif S[i]=='?':
    hatenalist.append(i)
  elif S[i]=='x':
    batsulist.append(i)
#print (marulist)
#print (batsulist)
count = 0
check = ''
for i in range(0,10000):
  #if str([j for j in batsulist]) in str(i):
   # continu
  if i<10:
    check = '000'+str(i)
  elif i<100:
    check = '00'+str(i)
  elif i<1000:
    check = '0'+str(i)
  else:
    check = str(i)   
  skip = False
  marucount =0
  for j in batsulist:
    if str(j) in check:
      skip =True
      break
  if skip ==True:
    skip = False
    continue
  for j in marulist:
    if str(j) in check:
      marucount+=1
  if marucount !=len(marulist):
    continue
  count+=1
  #print (i)
print (count)