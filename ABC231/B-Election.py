import collections
Slist =[]
N=int(input())
for _ in range(N):
  Slist.append(input())
c = collections.Counter(Slist)

print (c.most_common()[0][0])