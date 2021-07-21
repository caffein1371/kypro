a,b,c,d = map(int,input().split())
if min(d,b)-max(c,a)>0:
  print (min(d,b)-max(c,a))
else:
  print (0)