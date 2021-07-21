from collections import Counter
N = int(input())
Slist = []
for i in range(N):
  temp = str(input())
  Slist.append(''.join(sorted(temp)))

ans =0
c = Counter(Slist)
#print (c)
for i in c.values():
  #print (Slist.count(anslist[i]))
  if i>1:
    ans += (i*(i-1))//2
    #print (ans)
print (ans)