N = int(input())
Alist = list(map(int,input().split()))
import collections
Blist = list(set(Alist))
#print (Blist)
tmp =collections.Counter(Alist)
sumnum = N*(N-1)/2
#print (sumnum)
#print (tmp)
for i in range(len(Blist)):
  #print ("{} {} {}".format(Blist[i],tmp[Blist[i]],(tmp[Blist[i]]*(tmp[Blist[i]]-1))//2))
  sumnum-=(tmp[Blist[i]]*(tmp[Blist[i]]-1))/2
print (int(sumnum))