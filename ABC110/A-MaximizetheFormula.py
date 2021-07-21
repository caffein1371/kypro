anslist = list(map(int,input().split()))

anslist = sorted(anslist,reverse=True)
#print (anslist)

print (int(str(anslist[0])+str(anslist[1]))+anslist[2])