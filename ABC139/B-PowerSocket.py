A,B = map(int,input().split())
ans = 1
iter = 0
while True:
  if ans>=B:
    break
  ans-=1
  ans+=A
  iter+=1
  
print (iter)