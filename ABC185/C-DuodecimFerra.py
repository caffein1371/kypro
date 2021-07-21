import math
L = int(input())

ans = 1
for i in range(1,12):
  ans*=(L-i)

print (ans//math.factorial(11))