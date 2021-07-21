import math
n = int(input())
xlist = list(map(int,input().split()))
ylist = list(map(int,input().split()))

p1 = 0
for i in range(n):
  p1+=abs(xlist[i]-ylist[i])
print ('{:.6f}'.format(p1))

p2 = 0
for i in range(n):
  p2+=(xlist[i]-ylist[i])**2
  
p2 = math.sqrt(p2)
print ('{:.6f}'.format(p2))

p3 = 0
for i in range(n):
  p3+=abs((xlist[i]-ylist[i]))**3
p3 = p3**(1/3)
print ('{:.6f}'.format(p3))

pinf = 0
ans =[0]*n
for i in range(n):
  ans[i] = abs(xlist[i]-ylist[i])
  
print ('{:.6f}'.format(max(ans)))