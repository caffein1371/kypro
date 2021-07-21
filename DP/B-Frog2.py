N,K= map(int,input().split())
h = list(map(int,input().split()))
dp =[float('inf')]*N
dp[0]=0
for i in range(1,N):
  dp[i] = min(abs(h[i]-h[j])+dp[j] for j in range(max(0,i-K),i))
  
#print (dp)
print (dp[N-1])
