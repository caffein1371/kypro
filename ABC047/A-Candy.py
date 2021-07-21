clist = list(map(int,input().split()))
clist = sorted(clist)
if clist[0]+clist[1]==clist[2]:
  print ('Yes')
elif clist[0]==clist[1]+clist[2]:
  print ('Yes')
else:
  print ('No')