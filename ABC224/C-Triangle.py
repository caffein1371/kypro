import itertools
N = int(input())
XY = []
for _ in range(N):
  x,y = map(int,input().split())
  XY.append([x,y])
ans = 0
for v in itertools.combinations(XY,3):
  #print (v)
  if abs((v[0][0]-v[2][0])*(v[1][1]-v[2][1])-(v[1][0]-v[2][0])*(v[0][1]-v[2][1]))/2>0:
    ans+=1
print (ans)