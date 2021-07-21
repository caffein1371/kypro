import math
R,X,Y = map(int,input().split())
distance = math.sqrt(X*X+Y*Y)
count = math.ceil(distance/R)
# D<R
if count ==1 and distance<R :
  count +=1
print (int (count))