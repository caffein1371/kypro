N,K,A = map(int,input().split())
if ((K-1)%N+A)>N:
  print (((K-1)%N+A)%N)
else:
  print (((K-1)%N+A))