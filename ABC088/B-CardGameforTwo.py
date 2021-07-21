N = int(input())
Alist = list(map(int,input().split()))

Alist = sorted(Alist,reverse = True)
#print (Alist)
ans =0
for i in range(N):
  if i%2==0:
    ans+=Alist[i]
  else:
    ans-=Alist[i]
    
print (ans)