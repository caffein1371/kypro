N = input()

num = int(N)
ans = 0
for i in range(len(N)):
  ans+=int(N[i])
  
if num%ans==0:
  print ('Yes')
else:
  print ('No')