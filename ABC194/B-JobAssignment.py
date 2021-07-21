N = int(input())
anslist = []
alist = []
blist = []
for i in range(N):
  A,B = map(int,input().split())
  alist.append(A)
  blist.append(B)
  
amin = min(alist)
bmin = min(blist)
one = amin+bmin
two = max(amin,sorted(blist)[1])
three = max(bmin,sorted(alist)[1])
ans =[]
if alist.index(amin)!=blist.index(bmin):
  ans.append(max(amin,bmin))
  
#print (sorted(alist))
ans.append(one)
ans.append(two)
ans.append(three)

print (min(ans))