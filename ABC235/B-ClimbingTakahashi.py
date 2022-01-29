N=int(input())
Hlist = list(map(int,input().split()))
temp =-1
for i in range(N):
  if temp<Hlist[i]:
    temp = Hlist[i]
  else:
    break
print (temp)