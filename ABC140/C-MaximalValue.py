N = int(input())
Blist = list(map(int,input().split()))

Blist.reverse()
#print (Blist)
anslist = []
anslist.append(Blist[0])
for i in range(N-2):
  temp = Blist[i] if Blist[i]< Blist[i+1] else Blist[i+1]
  #print (temp)
  anslist.append(temp)

anslist.append(Blist[-1])    
print (sum(anslist))