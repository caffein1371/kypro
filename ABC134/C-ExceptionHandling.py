N = int(input())
alist = []
for i in range(N):
  alist.append(int(input()))

ans = 0
max1 = max(alist)
tempindex = alist.index(max1)
del alist[tempindex]
max2 =max(alist)

for i in range(N):
  if i!=tempindex:
    print (max1)
  else:
    print (max2)