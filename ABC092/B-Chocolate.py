N = int(input())
D,X =map(int,input().split())
Alist = []
for i in range(N):
  Alist.append(int(input()))

#print (Alist)
ans = X
for i in range(len(Alist)):
  for j in range(1,D+1,Alist[i]):
    ans+=1
    #print ('{}  {}'.format(ans,j))

print (ans)