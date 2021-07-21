N = int(input())
Hlist = list(map(int,input().split()))

ans = 0
alist = [0]
for i in range(N):
  if Hlist[i]>=max(alist):
    ans+=1
    alist.append(Hlist[i])
print (ans)