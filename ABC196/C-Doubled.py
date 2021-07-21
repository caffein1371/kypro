N = int(input())
ans = 0
for i in range(1,N):
  temp = int(str(i)+str(i))
  if temp>N:
    break
  ans +=1
print (ans)