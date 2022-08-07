import collections

Alist = list(map(int,input().split()))
c = collections.Counter(Alist)
anslist = sorted(list(c.values()))
if anslist[0]==2 and anslist[1]==3 and len(anslist)>=2:
  print ("Yes")
else:
  print ("No")