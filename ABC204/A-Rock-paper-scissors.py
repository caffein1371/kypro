x,y = map(int,input().split())
ans = [0,1,2]

if x==y:
  print (x)
else:
  ans.remove(x)
  ans.remove(y)
  print (ans[-1])