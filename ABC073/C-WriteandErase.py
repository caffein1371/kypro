import collections
N = int(input())
alist =[]
for i in range(N):
  temp = int(input())
  alist.append(temp)
c = collections.Counter(alist)
ans = 0
#print (c)
cl = [1 if i%2!=0 else 0 for i in c.values()]
print (sum(cl))