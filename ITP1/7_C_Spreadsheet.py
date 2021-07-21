r,c = map(int,input().split())
ans = [[0]*(c+1) for i in range(r+1)]
for i in range(r):
  ans[i] = list(map(int,input().split()))
  ans[i].append(sum(ans[i]))

for j in range(c+1):
  temp = 0
  for i in range(r+1):
    temp+=ans[i][j]
  ans[i][j]=temp
  
#print (ans)
for i in range(r+1):
  for j in range(c+1):
    if j==c:
      print (str(ans[i][j]))
    else :
      print (str(ans[i][j])+' ',end ='')