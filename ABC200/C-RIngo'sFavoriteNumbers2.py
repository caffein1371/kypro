N = int(input())
Alist = list(map(int,input().split()))
modlist = [Alist[i]%200 for i in range(N)]
#print (modlist)
setlist = list(set(modlist))
countlist = []
for i in range(len(setlist)):
  countlist.append(modlist.count(setlist[i]))
count =0
#print (countlist)
# ２つ以上あるものを組み合わせで二つあるのでnC2
for i in range(len(countlist)):
  count += countlist[i]*(countlist[i]-1)/2
print (int(count))