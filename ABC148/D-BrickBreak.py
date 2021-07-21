N= int(input())
alist =list(map(int,input().split()))

num=1
for i in range(N):
  if alist[i]==num:
    num+=1
  
if num!=1:
  print (N-num+1)
else:
  print (-1)