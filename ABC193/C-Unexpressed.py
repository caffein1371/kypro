import math

#print (math.log2(10**10))
#print (2**33)
#大体2の33乗まで
#print (3**21)

N = int(input())
ans=[]
for i in range(2,100000):
  for j in range(2,40):
    if 1<= i ** j <=N:
      ans.append(i**j)
    else:
      break
print (N-len(set(ans)))