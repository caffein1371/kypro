ori ='abcdefghijklmnopqrstuvwxyz'
X = input()
N = int(input())
d ={}
for i in range(len(X)):
  d[X[i]]=ori[i]
ans = {}
for _ in range(N):
  temp = input()
  tmp = ''
  for i in range(len(temp)):
    tmp+=str(d[temp[i]])
  ans[temp]=tmp
score_sorted = sorted(ans.items(), key=lambda x:x[1])
for i in range(len(ans)):
  print (score_sorted[i][0])