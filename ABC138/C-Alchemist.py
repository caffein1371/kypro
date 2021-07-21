N = int(input())
Vlist = list(map(int,input().split()))

Vlist = sorted(Vlist,reverse =False)
ave = 0
for i in range(len(Vlist)):
  if i ==0:
    ave = Vlist[i]
  else:
    ave = (ave+Vlist[i])/2
  
print (ave)