N = int(input())
Alist = list(map(int,input().split()))
X = int(input())
anssum = sum(Alist)
temp = X//anssum
anstemp = anssum*temp
for i in range(N):
  anstemp+=Alist[i]
  if anstemp>X:
    print (temp*N+i+1)
    quit()