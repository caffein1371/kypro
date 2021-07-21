S = input()

#ACGT = [A,C,G,T]
ans = 0
temp = 0
for i in range(len(S)):
  if S[i]=='A' or S[i]=='C' or S[i]=='G' or S[i]=='T':
    temp+=1
  else:
    temp =0
  if ans <temp:
    ans = temp
    
print (ans)