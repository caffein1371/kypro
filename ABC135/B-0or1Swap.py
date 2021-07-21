N = int(input())
plist = list(map(int,input().split()))

sortp = sorted(plist)
#print (sortp)
count = 0
for i in range(N):
  if plist[i]!=sortp[i]:
    count+=1
  if count >2:
    break
if count>2:
  print ('NO')
else:
  print ('YES')