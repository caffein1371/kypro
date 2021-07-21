alist = input()
blist = input()
for i in range(len(alist)):
  if alist[i]!=blist[len(blist)-i-1]:
    print ('NO')
    quit()
print ('YES')   