N,K = map(int,input().split())
count = 0
while K>count:
  #print (N)
  if N%200==0:
    N=N//200
  else:
    N = int(str(N)+'200')
  count +=1
print (N)