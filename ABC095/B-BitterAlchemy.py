N,X = map(int,input().split())
m = []
for i in range(N):
  m.append(int(input()))
nokori = X-sum(m)
print (N+nokori//min(m))