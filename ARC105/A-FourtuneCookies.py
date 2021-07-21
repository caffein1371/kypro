import itertools
Alist= list(map(int,input().split()))

Blist = Alist
ansflag = False
for i in range(1,5):
  for v in itertools.combinations(Alist, i):
    if sum(Alist)-sum(v)==sum(v):
      ansflag = True
      break
      
if ansflag ==True:
  print ('Yes')
else:
  print ('No')