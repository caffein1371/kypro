alist = list(map(int,input().split()))
alist =sorted(alist)
if alist[2]-alist[1]==alist[1]-alist[0]:
  print ('Yes')
else:
  print ('No')