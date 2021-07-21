S = input()

ans = True
for i in range(len(S)):
  if S.count(S[i])!=2:
    ans = False
    break
    
if ans is False:
  print ('No')
else :
  print ('Yes')