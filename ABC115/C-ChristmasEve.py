import itertools

N,K = map(int,input().split())
hlist =[]
for i in range(N):
  hlist.append(int(input()))

temp = 10**9
hlist = sorted(hlist)

for i in range(0,len(hlist)-K+1,1):
  #templist =hlist[i:i+K]
  temp = min(hlist[i+K-1]-hlist[i],temp)
  
print (temp)