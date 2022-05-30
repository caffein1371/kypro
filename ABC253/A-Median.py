alist=list(map(int,input().split()))
temp = sorted(alist)
if alist[1]==temp[1]:
  print ("Yes")
else:
  print ("No")