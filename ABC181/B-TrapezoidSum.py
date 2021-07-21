n = int(input())
ans = 0
for i in range(n):
  start,end = map(int,input().split())
  n = end-start+1
  sum = (1/2)*n*(2*start+(n-1))
  ans+=sum

print (int(ans))