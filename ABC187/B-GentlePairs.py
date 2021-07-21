import itertools
N = int(input())
xlist = []
ylist = []
xylist = [[0 for i in range(2)]for j in range(N)]
#print (xylist)
for i in range(N):
  x,y = map(int,input().split())
  xylist[i][0]=x
  xylist[i][1]=y

#print (xylist)
count = 0
for v in itertools.combinations(xylist,2):
  #print (v[0][0])
  #print ((v[1][1]-v[0][1])/(v[1][0]-v[0][0]))
  if ((v[1][1]-v[0][1])//(v[1][0]-v[0][0]))>=-1 and ((v[1][1]-v[0][1])/(v[1][0]-v[0][0]))<=1:
    count+=1
print (count)
    
    