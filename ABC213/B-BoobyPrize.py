N = int(input())
Alist = list(map(int,input().split()))
Blist = list(sorted(Alist,reverse=True))
print (Alist.index(Blist[1])+1)