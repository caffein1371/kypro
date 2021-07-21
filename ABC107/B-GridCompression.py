import numpy as np
H,W = map(int,input().split())
anslist = []
for i in range(H):
  temp = input()
  temp2 = []
  for j in range(len(temp)):
    if temp[j]=='#':
      temp2.append(1)
    else:
      temp2.append(0)
  anslist.append(temp2) 
#print (anslist)
templist =  np.array(anslist)
#print (templist)
#print (np.sum(templist,axis=1))
#print  (np.delete(templist,np.where(np.sum(templist,axis=1)==0),axis=0))
templist = np.delete(templist,np.where(np.sum(templist,axis=1)==0),axis=0)
#print  (np.delete(templist,np.where(np.sum(templist,axis=0)==0),axis=1))
templist = np.delete(templist,np.where(np.sum(templist,axis=0)==0),axis=1)
templist = np.where(templist==1,'#','.')
#print (templist)

for i in range(len(templist)):
  print (''.join(templist[i]))