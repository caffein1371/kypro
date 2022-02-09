import itertools
N = int(input())
L = []
R = []
for _ in range(N):
  t,l,r = map(int,input().split())
  if t==2:
    r=r-0.5
  elif t ==3:
    l=l+0.5
  elif t==4:
    l=l+0.5
    r=r-0.5
  L.append(l)
  R.append(r)
L.sort()
R.sort()
ans= 0
for i in range(N):
  for j in range(i+1,N):
    ans+=(max(L[i],L[j])<=min(R[i],R[j]))
print (ans)