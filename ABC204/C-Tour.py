import sys
sys.setrecursionlimit(10000)

N,M = map(int,input().split())
graph = [[] for _ in range(N)]
for i in range(M):
  n,m= map(int,input().split())
  graph[n-1].append(m-1)
def dfs(v):
  #global seen
  if temp[v]==True:
    return
  temp[v] = True
  for next_v in graph[v]:
    dfs(next_v)
count = 0
for i in range(N):
  temp = [False]*N
  dfs(i)
  count+=sum(temp)
print (count)