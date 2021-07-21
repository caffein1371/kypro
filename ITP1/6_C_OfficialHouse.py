kosya = [[[0]*10 for i in range(3)] for j in range(4)]


n = int(input())
for i in range(n):
  b,f,r,v = map(int,input().split())
  #print ("{} {} {} {}".format(b,f,r,v))
  kosya[b-1][f-1][r-1]+=v

for i in range(4):
  for j in range(3):
    print (" {} {} {} {} {} {} {} {} {} {}".format(kosya[i][j][0],kosya[i][j][1],kosya[i][j][2],kosya[i][j][3],kosya[i][j][4],kosya[i][j][5],kosya[i][j][6],kosya[i][j][7],kosya[i][j][8],kosya[i][j][9]))
  if i!=3:
    print ("####################")
