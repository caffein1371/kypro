N,S,D =map(int,input().split())

xylist =[]
for i in range(N):
  x,y =map(int,input().split())
  if x<S and D<y:
    xylist.append([x,y])
if len(xylist)>0:
  print ('Yes')
else:
  print ('No')