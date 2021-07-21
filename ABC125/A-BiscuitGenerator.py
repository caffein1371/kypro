A,B,T = map(int,input().split())

tmp = 0
ans = 0
i = 1
while True:
  tmp = i*A
  if tmp<T+0.5:
    ans +=B
  else:
    break
  i+=1
  
print (ans)