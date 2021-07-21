import itertools

N = int(input())
ans = []
for i in range(N):
  x,y = map(int,input().split())
  ans.append([x,y])
#print (ans)
flag = False
for v in itertools.combinations(ans,3):
  if (v[2][0]-v[1][0])*(v[1][1]-v[0][1])==(v[1][0]-v[0][0])*(v[2][1]-v[1][1]):
    flag =True
    
  
if flag ==True:
  print ('Yes')
else:
  print ('No')