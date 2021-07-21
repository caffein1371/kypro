N= int(input())
Vlist = list(map(int,input().split()))
Clist = list(map(int,input().split()))

ans1 = 0
ans2 = 0
ans = []
for i in range(N):
  ans.append(Vlist[i]-Clist[i])
lastans = 0
ans = sorted(ans,reverse=True)
for i in range(len(ans)):
  if ans[i]>0:
    lastans +=ans[i]
    
print (lastans)