import math
n = int(input())
while True:
  if n ==0:
    break
  alist = list(map(int,input().split()))
  a2 = 0
  mean = sum(alist)/n
  tempsum =0
  for i in range(n):
    tempsum+=(alist[i]-mean)*(alist[i]-mean)
  print ('{:8f}'.format(math.sqrt(tempsum/n)))
  n = int(input())