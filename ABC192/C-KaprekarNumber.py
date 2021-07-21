def calcurate(num):
  g = str(num)
  g1 =sorted(g,reverse= True)
  g1 = int(''.join(g1))
  g2 =sorted(g,reverse= False)
  g2 = int(''.join(g2))
  return g1-g2

N,K = map(int,input().split())

ans = N
while True:
  if K==0:
    print (ans)
    quit()
  elif K>0:
    K-=1
    ans = calcurate(ans)