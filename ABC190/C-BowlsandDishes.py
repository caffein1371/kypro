N,M =map(int,input().split())

xylist =[]
for i in range(M):
  a,b =map(int,input().split())
  xylist.append([a,b])
  
K = int(input())
cdlist = []
for i in range(K):
  c,d =map(int,input().split())
  cdlist.append([c,d])
#print (cdlist)
import itertools

#*を関数で渡すとタプル型渡すことができる．

maxcount = 0
for balls in itertools.product(*cdlist):
  print (balls)
  balls = set(balls)
  cnt = sum(A in balls and B in balls for A, B in xylist)
  if maxcount < cnt:
    maxcount = cnt
print (maxcount)