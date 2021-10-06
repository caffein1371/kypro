import numpy as np
N,K = map(int,input().split())
Alist = list(map(int,input().split()))
Blist = list(np.argsort(Alist))
#print (Clist)
temp = K//N
remain = K%N
ans = [temp]*N
for i in range(remain):
  ans[Blist[i]]+=1
for i in range(N):
  print (ans[i])