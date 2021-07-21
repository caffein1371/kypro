N = int(input())
Alist = list(map(int,input().split()))
Blist =set(Alist)
if len(Blist)!=len(Alist):
    print('No')
else:
    print ('Yes')