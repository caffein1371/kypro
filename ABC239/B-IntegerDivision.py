import math
X = input()
if int(X)>=0:
  if len(X)!=1:
    print ((X[0:-1]))
  else:
    print (0)
else:
  if int(X)<0 and int(X)>-10:
    print (-1)
    
  elif int(X[-1])==0:
    print ((-1)*int(X[1:-1]))
  else:
    print ((-1)*(int(X[1:-1])+1))