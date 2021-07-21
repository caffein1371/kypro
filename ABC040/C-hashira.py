N = int(input())
alist = list(map(int,input().split()))             
dp = [float('inf')]*N
dp[0] = 0
for i in range(1,N):
  dp[i] = min(dp[i],dp[i-1]+abs(alist[i]-alist[i-1]))
  if 1<i:
    dp[i] = min(dp[i],dp[i-2]+abs(alist[i]-alist[i-2]))

print (dp[N-1])