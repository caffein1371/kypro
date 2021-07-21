N = int(input())
tlist = []
xlist = []
ylist = []
tlist.append(0)
xlist.append(0)
ylist.append(0)
  
for i in range(N):
  t,x,y = map(int,input().split())
  tlist.append(t)
  xlist.append(x)
  ylist.append(y)
  
#print (tlist)
can =True
for i in range(N):
  dt = tlist[i+1]-tlist[i]
  dist = abs(xlist[i+1]-xlist[i])+abs(ylist[i+1]-ylist[i])
  if dt<dist:#変化量の総和がtをオーバーした時
    can = False
  if dist%2!=dt%2:#時間の変化量と移動量が奇数同士か偶数同士か
    can = False
if can ==True:
  print ('Yes')
else:
  print ('No')