S = input()
T = input()

ans = len(T)
for i in range(len(S)-len(T)+1):

  temp = 0
  for j in range(len(T)):
    print ('S={}'.format(S[i+j]))
    print ('T={}'.format(T[j]))
    if S[i+j]!=T[j]:
      temp+=1
  if ans>=temp:
    ans = temp
print (ans)