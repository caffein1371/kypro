N = int(input())
ans = []
for i in range(N):
  W = input()
  if i>=1:
    if W[0] !=temp[-1]:
      print ('No')
      quit()
    if W in ans:
      print ('No')
      quit()
  ans.append(W)
  temp = W
print ('Yes')