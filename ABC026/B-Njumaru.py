import math
N = int(input())
Rlist = []
for i in range(N):
  R= int(input())
  Rlist.append(R)
Rlist.sort()
anslist = []
for i in range(N):
  if i%2==0:
    anslist.append(Rlist[i]**2*math.pi)
  else:
    anslist.append(-Rlist[i]**2*math.pi)
print (abs(sum(anslist)))