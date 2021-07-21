import itertools
Alist = list(map(int,input().split()))

ans = 10000
for v in itertools.combinations(Alist,2):
  if ans>=sum(v):
    ans = sum(v)
print (ans)