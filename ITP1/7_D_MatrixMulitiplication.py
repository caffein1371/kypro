n,m,l = map(int,input().split())
matrix1 = [[0]*m for i in range(n)]
matrix2 = [[0]*l for i in range(m)]
#print (matrix1)
#print (matrix2)
for i in range(n):
  matrix1[i] = list(map(int,input().split()))
for i in range(m):
  matrix2[i] = list(map(int,input().split()))
                   
ans = [[0]*l for i in range(n)]
for i in range(n):
  for j in range(l):
    temp =0
    for k in range(m):
      #print ('{} {} {}'.format(i,j,l))
      #print ('{} * {}'.format(matrix1[i][k],matrix2[k][j]))
      temp+= matrix1[i][k]*matrix2[k][j]
    #print (temp)
    ans[i][j] =temp
#print (ans)
#print (c)
for i in range(n):
  print (str(ans[i][0]),end='')
  for j in range(1,l):
      print (' '+str(ans[i][j]),end='')
  print ()