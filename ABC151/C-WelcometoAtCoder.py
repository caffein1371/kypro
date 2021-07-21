N,M =map(int,input().split())
seikailist = [False for i in range(100001) ]
penaltylist = [0 for i in range(100001)]
seikai = 0
penalty = 0
num = 0
for i in range(M):
  p,S = map(str,input().split())
  if S=='WA' and seikailist[int(p)]==False:
    penaltylist[int(p)]+=1
  elif S=='AC':
    seikailist[int(p)]=True  
for i in range(100001):
  if seikailist[i]==True:
    seikai+=1
    penalty +=penaltylist[i]
#print (penaltylist)
#print (seikailist)
print ('{} {}'.format(seikai,penalty))