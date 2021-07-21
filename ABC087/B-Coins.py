A = int(input()) #500
B = int(input()) #100
C = int(input()) #50
X = int(input())

pattern = []
count =0
for i in range(A+1):
  ans = [0]*3
  ans[0]=i
  for j in range(B+1):
    ans[1]=j
    for k in range(C+1):
      ans[2]=k
      #print (ans)
      #pattern.append(ans)
      if (ans[0]*500+ans[1]*100+ans[2]*50)==X:
        count+=1
      
#print (pattern)
print (count)