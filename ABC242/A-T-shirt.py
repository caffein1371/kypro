A,B,C,X= map(int,input().split())

if A>=X:
  print (1.0000000)
elif B<X:
  print (0)
elif A+1<=X and X<=B:
  print (C/(B-A))
  