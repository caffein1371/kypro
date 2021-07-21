N = int(input())
Llist =list(map(int,input().split()))

maxnum = max(Llist)
if maxnum < sum(Llist)-maxnum:
  print ('Yes')
else:
  print ('No')