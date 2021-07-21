N = int(input())
alist = list(map(int,input().split()))
tansaku = [1,0,-1]
anslist = [0 for i in range(100001)]
for i in range(N):
  for j in range(3):
    if alist[i]+tansaku[j]>0:
      anslist[alist[i]+tansaku[j]]+=1
      #print (alist[i]+tansaku[j])
print (max(anslist))