n = int(input())
alist = list(map(int,input().split()))
d = {1:0,2:1,3:0,4:1,5:2,6:3,7:0,8:1,9:0}
ans = 0
for i in range(n):
  ans+=d[alist[i]]
print (ans) 