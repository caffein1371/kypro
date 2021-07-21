s = int(input())
f = []
f.append(s)
m = 10**7
ans = 0
for i in range(2,m):
  #print (f)
  if s%2==0:
    s = s//2
  else :
    s = 3*s+1
  if s in f:
    ans = i
    break
  f.append(s)

  
print (ans)