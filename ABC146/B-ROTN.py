alphabet =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

N = int(input())
S = input()
ans =[]
temp = 0
for i in range(len(S)):
  for j in range(len(alphabet)):
    if S[i]==alphabet[j]:
      #print (j)
      if j+N>=26:
        #print (alphabet[j+N-26])
        ans.append(alphabet[j+N-26])
      else :
        #print (alphabet[j+N])
        ans.append(alphabet[j+N])
        
#print (ans)
print (''.join(ans))