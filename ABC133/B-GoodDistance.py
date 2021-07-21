N,D = map(int,input().split())
Xlist = []
for i in range(N):
  x = list(map(int,input().split()))
  Xlist.append(x)
import itertools
import math
#print (Xlist)
ans = 0
count =0
for v in itertools.combinations(Xlist,2):
  #print (v)
  ans =0
  for j in range(D):
    ans += (v[0][j]-v[1][j])**2
  #print (math.sqrt(ans))
  if math.sqrt(ans).is_integer() is True:
    count+=1
    
print (count) 
