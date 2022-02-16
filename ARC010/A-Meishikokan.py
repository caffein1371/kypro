N,M,A,B = map(int,input().split())
C = []
ans =0
for i in range(M):
  if N<=A and N>=0:
    N+=B
  c = int(input())
  N-=c
  if N<0:
    ans=i+1
    break

if N>=0:
  print ("complete")
else:
  print (ans)