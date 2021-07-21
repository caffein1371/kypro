N,A,B = map(int,input().split())
S = input()
tuka = 0
rank = 1
for i in range(N):
  #print (S[i])
  if S[i]=='a' and tuka<A+B:
    tuka+=1
    print ('Yes')
  elif S[i]=='b' and tuka<A+B and rank<=B:
    tuka+=1
    rank+=1
    print ('Yes')
  elif S[i]=='c':
    print ('No')
  else:
    print ('No')
    