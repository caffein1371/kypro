N = int(input())
Alist = list(map(int,input().split()))
ans = [0]
for i in range(N):
  ans = list(map(lambda x : x+Alist[i],ans))
  ans = list(map(lambda x :x if x<360 else x%360 , ans))
  ans.insert(0,0)
  ans.sort()
  #print (ans)
ans.append(360)
maxn = 0
for i in range(len(ans)-1):
  maxn = max(maxn,abs(ans[i]-ans[i+1]))
print (maxn)