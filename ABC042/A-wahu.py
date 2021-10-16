A = list(map(int,input().split()))

try:
  A.remove(5)
except:
  print ("NO")
  quit()
try:
  A.remove(7)
except:
  print ("NO")
  quit()
try:
  A.remove(5)
except:
  print ("NO")
  quit()
if len(A)==0:
  print ("YES")
else:
  print ("NO")