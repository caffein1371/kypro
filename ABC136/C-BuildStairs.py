N = int(input())
Hlist = list(map(int,input().split()))

ansflag = True
Hlist = Hlist[::-1]
#print (Hlist)
for i in range(N-1):
  if Hlist[i]<Hlist[i+1]:
    Hlist[i+1]-=1
  if Hlist[i]<Hlist[i+1]:
    ansflag =False
    break
  
if ansflag is True:
  print ('Yes')
else:
  print ('No')