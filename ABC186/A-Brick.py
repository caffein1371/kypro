N,W = map(int,input().split())

ans = 1
while W*ans<=N:
  ans+=1
  
print (ans-1)