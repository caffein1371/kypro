N = int(input())
Alist = list(map(int,input().split()))

ans =[0]*(N+1)
for i in range(N):
  #print (sum(Alist[i+1:N]))
  ans[i+1] =Alist[i]+ans[i]
#print (ans)

answer = 0
for i in range(N):
  sumans = ans[N]-ans[i+1]
  answer+= Alist[i]*sumans
print (answer%(10**9+7))