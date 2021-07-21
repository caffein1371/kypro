alist =[]
temp = 0
for i in range(6):
  alist.append(int(input()))
ans = True
for i in range(len(alist)):
  if i==0:
    temp = alist[i]
  else:
    if alist[i]-temp>alist[5]:
      ans =False
      break
if ans is False:
  print (':(')
else:
  print ('Yay!')