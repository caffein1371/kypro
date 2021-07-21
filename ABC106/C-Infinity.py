S = input()
K = int(input())
#print (S)
#print (K)
ans = []
temp = 0
K-=1
for i in range(len(S)):
  if S[i]=="1":
    if K==0:
      print ('1')
      quit()
    else :
      K-=1
  elif S[i]!='1':
    print (S[i])
    quit()