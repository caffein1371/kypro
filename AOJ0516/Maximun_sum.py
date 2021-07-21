import itertools
while True:
  n,k = map(int,input().split())
  if n ==0 and k ==0:
    quit()
  anslist =[]
  for i in range(n):
    anslist.append(int(input()))
    #print (anslist)
  ac = list(itertools.accumulate(anslist))
  #print (ac)
  maxtemp = -float('inf')
  for i in range(0,n-k):
    #print ('i={}'.format(i))
    #print (ac[i+k]-ac[i])
    if maxtemp <ac[i+k]-ac[i]:
      maxtemp = ac[i+k]-ac[i]
  print (maxtemp)