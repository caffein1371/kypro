S = input()
T = input()
for i in range(len(S)):
  if S == T:
    print ('Yes')
    quit()
  temp = S[-1]
  S = S[0:len(S)-1]
  S = temp+S
  #print (S)  
print ('No')