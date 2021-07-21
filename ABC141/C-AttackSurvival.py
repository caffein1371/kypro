import numpy as np
N,K,Q = map(int,input().split())

#points =  np.array([K]*N)
points = np.full(N, K)
#print (points)
ans = []
#for i in range(Q):
 # a = int(input())
  #ans.append(a)
a = [int(input()) for _ in range(Q)]
#print (a)

for i in range(len(a)):
  points-=1
  #points = map(lambda x: x+1, points)
  points[a[i]-1]+=1
  #for j in range(N):
   # if j!=(a-1):
    #  points[j]-=1
#print (points)
for i in range(N):
  if points[i]>0:
    print ('Yes')
  else:
    print ('No')