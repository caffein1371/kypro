N = int(input())
Alist = list(map(int,input().split()))
Blist = list(map(int,input().split()))

if min(Blist)-max(Alist)<0:
  print(0)
else:
  print (min(Blist)-max(Alist)+1)