N,W =map(int,input().split())
value = [0]*N
weight = [0]*N
for i in range(N):
  value[i],weight[i] = map(int,input().split())

dp = [[0]*(W+1) for j in range(N+1)] # DPテーブルの作成

for i in range(N):
    for j in range(W+1):
        if j < weight[i]: # 選ばない時
            dp[i+1][j] = dp[i][j]
        else: # 選ぶ時
            dp[i+1][j] = max(dp[i][j],dp[i][j-weight[i]]+value[i])
print (dp[N][W])