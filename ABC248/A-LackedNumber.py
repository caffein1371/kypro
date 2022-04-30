S=list(input())
S.sort()
for i in range(10):
  if S[i]!=str(i):
    print (i)
    quit()
  
print (9)