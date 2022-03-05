L,H = map(int,input().split())
N = int(input())
for i in range(N):
  A = int(input())
  if A<L:
    print (L-A)
  elif L<=A and A<=H:
    print (0)
  elif H<A:
    print (-1)