import math
X = int(input())
if X ==1:
  print (1)
  quit()
ans = 1
for i in range(2,1000):
  for j in range(2,10):
    if i**j<=X and ans<=i**j:
      ans =i**j
      #print ('{} {}'.format(i,j))
    if i**j>X:
      continue
print (ans)