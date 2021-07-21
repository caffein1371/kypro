#https://drken1215.hatenablog.com/entry/2020/12/19/231000
N = int(input())
Alist = list(map(int,input().split()))
Alist = sorted(Alist,reverse =False)
ruiseki = [0]*(N+1)
temp = 0
for i in range(0,N):
  ruiseki[i+1]= Alist[i]+temp
  temp =ruiseki[i+1]
  #print (ruiseki[i])
  
#print (ruiseki)

ruiseki2 = 0

for i in range(N):
  ruiseki2+= (i)*Alist[i]-ruiseki[i]
print (ruiseki2)