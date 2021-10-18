N = int(input())
Alist = list(map(int,input().split()))
Blist = sorted(set(Alist))
ans = 0
for i in range(len(Blist)-1):
  ans+= abs(Blist[i]-Blist[i+1])
print (ans)