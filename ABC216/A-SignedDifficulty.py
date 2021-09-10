X,Y = map(int,input().split("."))
if 0<=Y and Y<=2:
  print (str(X)+"-")
elif 3<=Y and Y<=6:
  print (X)
elif 7<=Y and Y<=9:
  print (str(X)+"+")