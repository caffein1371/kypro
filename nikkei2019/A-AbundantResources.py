N = int(input())
Alist =list(map(int,input().split()))

souryou = [0]*(N+1)
temp = 0
for i in range(N):
  souryou[i+1] = Alist[i]+souryou[i]
#print (souryou)
  
for k in range(1,N+1):
  ans = 0
  #print ('k= {}'.format(k))
  for i in range(0,N-k+1):
    #print ('i= {}'.format(i))
    #print (souryou[i+k]-souryou[i])
    if ans<=souryou[i+k]-souryou[i]:
      ans = souryou[i+k]-souryou[i]
  print (ans)