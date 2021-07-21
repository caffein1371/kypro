N,M = map(int,input().split())
maxl = 0
minr = 10**5
for i in range(M):
  l,r = map(int,input().split())
  if l >maxl:
    maxl =l
  if r <minr:
    minr = r
if minr - maxl>=0:
  print (minr-maxl+1)
else:
  print (0)