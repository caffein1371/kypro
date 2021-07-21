N = int(input())
Alist1 = list(map(int,input().split()))
Alist2 = list(map(int,input().split()))
leng = N
tempmax = -1
for i in range(leng):
  count = sum(Alist1[0:i+1])+sum(Alist2[i:leng])
  #print ('A1{} A2{}'.format(Alist1[0:i+1],Alist2[i:leng]))
  if count>tempmax:
    tempmax = count
print (tempmax)