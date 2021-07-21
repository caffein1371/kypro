from collections import Counter
N= int(input())
Alist = list(map(int,input().split()))
C = Counter(Alist).items()
#print (C)
ans=0
for i1,v1 in C:
  for i2,v2 in C:
    if i1>i2:
      continue
    if i1==i2:
      continue
    ans+=(i1-i2)**2*v1*v2
print (ans)