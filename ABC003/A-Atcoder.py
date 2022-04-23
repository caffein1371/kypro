N=int(input())
ans=0
for i in range(1,N+1):
  ans+=i*10000*1/N
print (int(ans))