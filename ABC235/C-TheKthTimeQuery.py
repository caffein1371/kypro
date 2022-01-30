from collections import defaultdict

N,Q = map(int,input().split())
Alist = list(map(int,input().split()))

Qlist = defaultdict(list)
for i in range(N):
  Qlist[Alist[i]].append((i+1))

for _ in range(Q):
  x,k = map(int,input().split())
  if len(Qlist[x])>=k:
    print (Qlist[x][k-1])
  else:
    print (-1)