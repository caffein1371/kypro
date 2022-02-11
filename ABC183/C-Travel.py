import itertools
from collections import defaultdict

N,K = map(int,input().split())
root = defaultdict(list)
a = [i+1 for i in range(N-1)]
for i in range(N):
  Rlist = list(map(int,input().split()))
  root[i] = Rlist
#print (root)
ans = 0
for v in itertools.permutations(a,N-1):
  score = 0
  prev = 0
  for i in v:
    score+=root[prev][i]
    prev = i
  score+= root[prev][0]
  if score == K:
    ans+=1
    
print (ans)