N,P = map(int,input().split())
Alist = list(map(int,input().split()))
ans = 0
for i in range(N):
  if Alist[i]<P:
    ans+=1
print (ans)