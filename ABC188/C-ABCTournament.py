def touranament(Alist):
  alist = []
  for i in range(0,len(Alist)-1,2):
    if Alist[i]>Alist[i+1]:
      alist.append(Alist[i])
    else:
      alist.append(Alist[i+1])
      
  return alist

N = int(input())
Alist = list(map(int,input().split()))
alist = Alist
while len(alist)>2:
  #print (alist)
  alist = touranament(alist)

minans= min(alist)
#print (minans)

print (Alist.index(minans)+1)