Alist = list(map(int,input().split()))
import itertools
#3!なので余裕らしい
mintemp =100000
for v in itertools.permutations(Alist):
  if mintemp>=abs(v[1]-v[0])+abs(v[1]-v[2]):
    mintemp= abs(v[0]-v[1])+abs(v[1]-v[2])
print (mintemp)