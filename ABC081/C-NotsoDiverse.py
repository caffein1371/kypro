import collections
n,k = map(int,input().split())
alist = list(map(int,input().split()))
alist = sorted(alist)
blist = list(set(alist))
#print (len(blist))
if len(blist)<=k:
  print ('0')
  quit()
c = collections.Counter(alist)
#product_list = ["A", "B"]
countlist = c.most_common()[::-1]
ans = 0
for i in range(len(countlist)):
  if len(blist)-i>k:
    ans+=countlist[i][1]
  else:
    break 
#print(countlist)
#print(countlist[0][1])
print(ans)