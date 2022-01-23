import bisect
N,Q =map(int,input().split())
Alist = list(map(int,input().split()))
Alist.sort()
print (Alist)
for _ in range(Q):
  temp = int(input())
  bis = bisect.bisect_left(Alist,temp)
  print (N-bis)