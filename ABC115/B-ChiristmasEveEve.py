N = int(input())
plist = []
for i in range(N):
  p = int(input())
  plist.append(p)
  
plist = sorted(plist)
plist[-1] = plist[-1]//2
print (sum(plist))