import itertools

def maxtime(x):
  return (x+9)//10*10

ans = []
for _ in range(5):
  ans.append(int(input()))
count = 10**7

for v in itertools.permutations(ans):
  #print (v)
  temp =0
  for i in range(len(v)):
    if i!=len(v)-1:
      temp+= maxtime(v[i])
    else:
      temp+= v[i]
    #print (temp)
  if temp<count:
    count = temp
      
print (count)
      