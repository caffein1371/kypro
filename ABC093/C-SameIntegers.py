anslist = list(map(int,input().split()))
#print (sorted(anslist))
count = 0
while True:
  anslist = sorted(anslist)
  #print ('{} {} {}'.format(anslist[0],anslist[1],anslist[2]))
  if anslist[0]==anslist[2]:
    print (count)
    quit()
  if anslist[2]-anslist[0]>=2:
    anslist[0]+=2
  elif anslist[2]-anslist[0]==1:
    anslist[0]+=1
    anslist[1]+=1 
  count+=1