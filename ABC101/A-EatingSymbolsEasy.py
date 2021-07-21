S = input()
ans = 0
for i in range(len(S)):
  if S[i]=='+':
    ans+=1
  elif S[i]=='-':
    ans-=1
print (ans)