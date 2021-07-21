import numpy as np
N = int(input())
Alist = list(map(int,input().split()))
Alist = np.array(Alist)
#print (Alist)
ans = 0
flag =True
while flag:
  #print(Alist)
  for i in range(len(Alist)):
    if Alist[i]%2!=0:
      flag = False
      break
    else:
      Alist[i] = Alist[i]//2
  if flag ==True:
    ans+=1
    
print (ans)