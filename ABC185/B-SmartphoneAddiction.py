N,M,T = map(int,input().split())
ori = N
anslist = []
for i in range(M):
  ans = list(map(int,input().split()))
  anslist.append(ans)
  
bat = N
time = 0
for i in range(M):
  bat -= anslist[i][0]-time
  #print ("{}-{}".format(anslist[i][0],time))
  #print (bat)
  if bat <=0:
    break
  if bat+anslist[i][1]-anslist[i][0]>=N:
    bat = N
    #print ("{} {}".format(anslist[i][1],anslist[i][0]))
  else:
    bat +=anslist[i][1]-anslist[i][0]
    #print ("{} {}".format(anslist[i][1],anslist[i][0]))
  #print (bat)
  time = anslist[i][1]
  if i==M-1:
    bat -=T-time
    #print ("{}- {}".format(T,time))
    time = T
#print (time)
#print (bat)

if bat >0:
  print ('Yes')
else:
  print ('No')