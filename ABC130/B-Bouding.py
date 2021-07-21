N,X = map(int,input().split())
Llist = list(map(int,input().split()))

D = [0]
ans = [0]
for i in range(1,N+1):
  temp = D[i-1]+Llist[i-1]
  D.append(temp)
  if temp <=X:
    ans.append(temp)
  
print (len(ans))