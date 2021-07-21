N= int(input())
height = list(map(int,input().split()))
dp =[float('inf')]*N
dp[0]=0
for i in range(N-1):
  if i<N-1:
    dp[i+1] = min(dp[i+1],dp[i]+abs(height[i]-height[i+1]))
    #print (abs(height[i]-height[i+1]))
  if i<N-2:
    dp[i+2] = min(dp[i+2],dp[i]+abs(height[i]-height[i+2]))
    #print (abs(height[i]-height[i+2]))
print (dp[-1])