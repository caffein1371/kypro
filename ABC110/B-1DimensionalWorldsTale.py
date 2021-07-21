N,M,X,Y = map(int,input().split())
xlist = list(map(int,input().split()))
ylist = list(map(int,input().split()))

for i in range(X+1,Y+1):
  if i > max(xlist) and i<= min(ylist):
    print ('No War')
    quit()
    
print ('War')