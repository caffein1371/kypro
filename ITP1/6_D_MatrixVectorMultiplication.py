n,m = map(int,input().split())
a = []
for i in range(n):
  gyouretsu = list(map(int,input().split()))
  a.append(gyouretsu)
b = []
for i in range(m):
  inp = int(input())
  b.append(inp)

ans =[0]*n
for i in range(n):
  for j in range(m):
    ans[i]+= a[i][j]*b[j]
for i in range(n):
  print (ans[i])