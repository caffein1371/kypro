A,B,K = map(int,input().split())
ans = []
for i in range(0,K):
  if A+i<=B:
    ans.append(A+i)
for i in range(K-1,-1,-1):
  if B-i>=A:
    ans.append(B-i)
ans = sorted(list(set(ans)))
for i in range(len(ans)):
  print (ans[i])