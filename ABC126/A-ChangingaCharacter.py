N,K = map(int,input().split())
S = input()
for i in range(N):
  if i!=N-1:
    if i==K-1:
      print (S[i].lower(),end ='')
    else:
      print (S[i],end ='')
  else :
    if i==K-1:
      print (S[i].lower())
    else:
      print (S[i])