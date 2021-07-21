N = int(input())
Alist = list(map(int,input().split()))
ans = 0
for i in range(len(Alist)):
  if Alist[i]>10:
    ans+=Alist[i]-10
print (ans)