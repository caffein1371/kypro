S= input()
ans =[]
i=0
while len(ans)<6:
  ans.append(S[i])
  i+=1
  if len(S)<=i:
    i=0
print ("".join(ans))