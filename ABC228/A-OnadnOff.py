S,T,X = map(int,input().split())
if S>T:
  T = T+24
if S>X:
  X = X+24

if S<=X and X<T:
  print ("Yes")
else:
  print ("No")