##########################################
import io
import sys

_INPUT = """\
4 3
3 14 15 92
6 53 58




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,M = map(int,input().split())
Alist = list(map(int,input().split()))
Blist = list(map(int,input().split()))
from collections import defaultdict
c = defaultdict(int)

Clist = Alist+Blist
Clist = sorted(Clist)
#print (Clist)
for i in range(N+M):
    c[Clist[i]]=i+1

#print (c)
#print (b)
for i in range(N):
    if N-1!=i:
        print (c[Alist[i]],end =' ')
    elif N-1==i:
        print (c[Alist[i]])
for j in range(M):
    if M-1!=j:
        print (c[Blist[j]],end =' ')
    elif M-1==j:
        print (c[Blist[j]])
