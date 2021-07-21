A,B = map(int,input().split())
    
if abs(A+B)%2==0:
  print (abs(A+B)//2)
else:
  print ('IMPOSSIBLE')