N,A,B = map(int,input().split())
ans = 0
for i in range(1,N+1):
  tempstr = str(i)
  tempans = 0
  for j in range(len(tempstr)):
    tempans+=int(tempstr[j])
  #print (tempans)
  if A<=tempans and tempans<=B:
    ans+=i
print (ans)