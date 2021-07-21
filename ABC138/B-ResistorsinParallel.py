N = int(input())
Alist = list(map(int,input().split()))
  
ans = 0
for i in range(N):
  ans+=1/Alist[i]
print (1/ans)