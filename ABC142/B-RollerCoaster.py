N,K = map(int,input().split())
hlist = list(map(int,input().split()))

count =0
for i in range(len(hlist)):
  if hlist[i]>=K:
    count+=1
    
print (count)