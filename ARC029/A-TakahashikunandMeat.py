import itertools
N = int(input())
tlist = []
for i in range(N):
  tlist.append(int(input()))

pattern = []
for i in range(2**N):
  ans = []
  for j in range(N):
    if (i>>j) &1:
      ans.append(j)
  #print (ans)
  pattern.append(ans)
  
answer = 1000000
for i in range(len(pattern)):
  min1 = 0
  min2 = 0
  for j in range(len(pattern[i])):
    #print ('pattern:{}'.format(pattern[i][j]))
    #print (tlist[pattern[i][j]])
    min1 += tlist[pattern[i][j]]
    
  min2 = sum(tlist)-min1
  #print ('{} {}'.format(min1,min2))
  temp = min1 if min1>min2 else min2
  if answer>temp:
    answer = temp
print (answer)
