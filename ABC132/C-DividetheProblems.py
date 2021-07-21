N =int(input())
dlist =list(map(int,input().split()))

dlist = sorted(dlist)
#print (dlist)
center1 = dlist[(len(dlist)//2)-1]
center2 = dlist[(len(dlist)//2)]

#print (center2)
#print (center1)
print (center2-center1)