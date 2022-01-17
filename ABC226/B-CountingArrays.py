from collections import defaultdict
d = defaultdict(int)
N = int(input())
ans =[]
for _ in range(N):
  alist = list((map(int,input().split())))
  ans.append(str(alist[1::]))
print (len(list(set(ans))))