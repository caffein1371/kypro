mod = (10**9)+7
N = int(input())
ans = 0
Clist = list(map(int,input().split()))
Clist.sort()
#print (Clist)
ans =1
for i in range(N):
  ans=ans*(Clist[i]-i)%mod
print (ans)