N = int(input())
Plist = list(map(int,input().split()))
temp = float('inf')
ans = 0
for i in Plist:
  if i < temp:
    temp = i
    ans += 1
print (ans)