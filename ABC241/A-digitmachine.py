Alist = list(map(int,input().split()))
temp =Alist.index(0)
for i in range(4):
  temp = Alist[temp]
print (temp)