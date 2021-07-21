n,m,x = map(int,input().split())
alist = list(map(int,input().split()))
plus = 0
for i in range(m):
  if x<alist[i]:
    plus +=1
print (min(plus,m-plus))