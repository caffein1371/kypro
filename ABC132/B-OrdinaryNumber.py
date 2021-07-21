n = int(input())
plist = list(map(int,input().split()))
count = 0
for i in range(1,n-1):
  #print (plist[i])
  if (plist[i]>plist[i-1] and plist[i+1]>plist[i]) or (plist[i]<plist[i-1] and plist[i+1]<plist[i]):
    count+=1
print (count)