A,B = map(str,input().split())
A=A[::-1]
B=B[::-1]
minsize = min(len(A),len(B))
for i in range(minsize):
  if int(A[i])+int(B[i])>=10:
    print ("Hard")
    quit()
print ("Easy")
                 