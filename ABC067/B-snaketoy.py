N,K = map(int,input().split())
Llist = list(map(int,input().split()))
templist = sorted(Llist,reverse=True)
print (sum(templist[0:K]))