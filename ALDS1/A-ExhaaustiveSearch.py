import itertools

n = int(input())
nlist = list(map(int,input().split()))
m = int(input())
mlist = list(map(int,input().split()))
anslist = []    
for i in range(1,n+1):
  for v in itertools.combinations(nlist,i):
    anslist.append(sum(v))

ans =[]
for i in range(len(mlist)):
  answer = 'no'
  for j in range(len(anslist)):
    answer = 'no'
    if mlist[i]==anslist[j]:
      answer = 'yes'
      break
  ans.append(answer)
for i in range(len(ans)):
  print (ans[i])