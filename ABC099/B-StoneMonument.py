a,b = map(int,input().split())
temp = b-a
ans = 0
for i in range(temp+1):
  ans+=i
print (ans-b)