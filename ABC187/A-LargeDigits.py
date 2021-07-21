A,B = map(str,input().split())

sumA=0
sumB=0
for i in range(3):
  sumA +=int(A[i])
  sumB +=int(B[i])
  
if sumA>=sumB:
  print (sumA)
else:
  print (sumB)