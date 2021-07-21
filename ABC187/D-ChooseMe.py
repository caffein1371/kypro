N = int(input())
Sumlist = []
Alist = []
Blist = []
for i in range(N):
  A,B = map(int,input().split())
  Alist.append(A)
  Blist.append(B)
  Sumlist.append(2*A+B)

sigma = sum(Alist)
  
Sumlist = sorted(Sumlist,reverse = True)
#print (Sumlist)
X = sigma*(-1)
ans = -1
for i in range(len(Sumlist)):
  X+=Sumlist[i]
  if X>0:
    ans = i
    break
print (ans+1)