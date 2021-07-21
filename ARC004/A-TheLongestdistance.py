import itertools
import math

N = int(input())
anslist =[]
    
for i in range(N):
  pointlist = list(map(int,input().split()))
  anslist.append(pointlist)

ans = 0
for v in itertools.combinations(anslist,2):
  #print (v)
  #print (v[0])
  #print (v[0][0])
  if ans<=math.sqrt(((v[0][0]-v[1][0])**2)+((v[0][1]-v[1][1])**2)):
    ans=math.sqrt(((v[0][0]-v[1][0])**2)+((v[0][1]-v[1][1])**2))
print ('{:.6f}'.format(ans))