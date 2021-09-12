import math
P = int(input())
ans =0
for i in range(10,0,-1):
  m = math.factorial(i)
  if m<=P:
    ans+= P//m
    P = P%m
print (ans)