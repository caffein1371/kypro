N = int(input())
xlist = []
ulist = []
ans = 0
for i in range(N):
  x,u = map(str,input().split())
  if u == 'JPY':
    ans+=int(x)
  elif u =='BTC':
    ans+=380000.0*float(x)
    
print (ans)