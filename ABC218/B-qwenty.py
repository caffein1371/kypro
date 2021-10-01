plist = list(map(int,input().split()))
for i in range(len(plist)):
  if len(plist)-1==i:
    print (chr(plist[i]+96))
  else:
    print (chr(plist[i]+96),end="")
  