N=int(input())
ans = 0
for i in range(N):
  temp = set(list(map(int,input().split())))
  ans += max(temp)-min(temp)+1
print (ans)