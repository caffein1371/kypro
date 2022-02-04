import numpy as np
H,W = map(int,input().split())
Alist = []
for i in range(H):
  A = list(map(int,input().split()))
  Alist.append(A)
arr = np.array(Alist)
arr = arr.T
arr = list(arr)
for i in range(W):
  for j in range(H):
    if j!=H-1:
      print (arr[i][j], end=' ')
    else:
      print (arr[i][j])