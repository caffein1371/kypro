S = input()
ans = 0
for i in range(len(S)):
  if (i+1)%2==1:
    ans+=int(S[i])
  else:
    ans-=int(S[i])
print (ans)