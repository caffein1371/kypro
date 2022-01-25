from collections import defaultdict
N = int(input())
Alist = list(map(int,input().split()))
d = defaultdict(int)
for i in range(len(Alist)):
  d[Alist[i]]+=1
#print (d)
for i in range(1,len(d)+1):
  if d[i]!=4:
    print (i)
    break