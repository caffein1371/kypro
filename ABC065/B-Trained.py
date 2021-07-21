N = int(input())
alist =[0]
count = 0
for i in range(N):
  temp = int(input())
  alist.append(temp) 
#print (alist)
#mention(alist,1,count,kioku)
temp = 1
while(1):
  if temp==2:
    print (count)
    quit()
  temp = alist[temp]
  count+=1
  if count>=N+1:
    break
print (-1)
    