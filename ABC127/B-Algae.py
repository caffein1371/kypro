r,D,x = map(int,input().split())

temp = x
for i in range(10):
  print (temp*r-D)
  temp = temp*r-D
