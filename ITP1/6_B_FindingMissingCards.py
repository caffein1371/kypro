ans = [[False for i in range(13)] for j in range(4)]
n = int(input())
for i in range(n):
  g,n = map(str,input().split())
  if g =='S':
    ans[0][int(n)-1]=True
  elif g=='H':
    ans[1][int(n)-1]=True
  elif g=='C':
    ans[2][int(n)-1]=True
  elif g=='D':
    ans[3][int(n)-1]=True
    
for i in range(4):
  for j in range(13):
    if i==0 and ans[i][j]==False:
      print ("S {}".format(j+1))
    elif i==1 and ans[i][j]==False:
      print ("H {}".format(j+1))
    elif i==2 and ans[i][j]==False:
      print ("C {}".format(j+1))
    elif i==3 and ans[i][j]==False:
      print ("D {}".format(j+1))