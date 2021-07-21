N = int(input())
Alist = list(map(int,input().split()))
Blist = list(map(int,input().split()))

ans = 0
for i in range(N):
  ans += Alist[i]*Blist[i]
  
if ans ==0:
  print ('Yes')
else:
  print ('No')