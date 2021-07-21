N = int(input())
alist = list(map(int,input().split()))

maxcount = 0
ans = 0
count = 0
for i in range(2,1001):
  count = 0
  for j in range(N):
    if alist[j]%i==0:
      #print ('{} {}'.format(alist[j],alist[i]))
      count+=1
      #print (count)
    #print ('{} {}'.format(count,maxcount))
  if count>=maxcount:
    maxcount = count
    ans = i
    #print (ans)
    
print (ans)