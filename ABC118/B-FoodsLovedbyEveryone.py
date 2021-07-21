N,M = map(int,input().split())

nlist = []
for i in range(N):
  n = list(map(int,input().split()))
  del n[0]
  nlist.append(n)
  
ans = 0

templist = set(nlist[0])
for l in nlist:
  nlist = set(l)
  templist = set(list(templist & nlist))
  
print (len(templist))
  