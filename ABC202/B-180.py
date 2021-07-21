S = input()
S = S[::-1]
ans = []
for i in range(len(S)):
  if S[i]=='9':
    ans.append('6')
  elif S[i]=='6':
    ans.append('9')
  else:
    ans.append(S[i])
print (''.join(ans))