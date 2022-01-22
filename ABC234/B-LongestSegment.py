import math
import itertools
def kyori(comblist):
  x1 = comblist[0][0]
  x2 = comblist[1][0]
  y1 = comblist[0][1]
  y2 = comblist[1][1]
  return (math.sqrt((x1-x2)**2+(y1-y2)**2))

N = int(input())
xylist =[]
for _ in range(N):
  x,y = map(int,input().split())
  xylist.append((x,y)) 
#print (list(itertools.combinations(xylist,2)))
comblist = list(itertools.combinations(xylist,2))
dis = -1
for i in range(len(comblist)):
  dis = max(kyori(comblist[i]),dis)
  
print (dis)