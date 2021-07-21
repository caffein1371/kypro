N,K = map(int,input().split())
alist = list(map(int,input().split()))

sumlist = [0]*(N+1)
for i in range(N):
  sumlist[i+1] = alist[i]+sumlist[i]

#print (sumlist)
ans = 0
for i in range(N-K+1):
  #print ('{} {}'.format(sumlist[i+K],sumlist[i]))
  ans+=sumlist[i+K]-sumlist[i]
print (ans)