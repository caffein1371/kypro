N = int(input())
Slist =[]
Slist2 = [] 
for i in range(N):
  temp = input()
  Slist.append(temp[::-1])

Slist = sorted(Slist)
#print (Slist)
ans = False

for i in range(N-1):
  #print (Slist[i])
  #print (Slist[i+1])
  if Slist[i]+'!'==Slist[i+1]:
    print (Slist[i][::-1])
    ans =True
    break
    
if ans ==False:
  print ('satisfiable')
