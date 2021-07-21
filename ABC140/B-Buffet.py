N = int(input())
Alist = list(map(int,input().split()))
Blist = list(map(int,input().split()))
Clist = list(map(int,input().split()))

ans = 0
temp = -2
for i in range(N):
  #print (Alist[i])
  #print (ans)
  #print ('Alist {} temp {}'.format(Alist[i],temp))
  if temp+1==Alist[i]:
    ans+=Clist[Alist[i]-2]
  ans+=Blist[Alist[i]-1]
  temp = Alist[i]
  #print ('temp{}'.format(temp))
  
print (ans)