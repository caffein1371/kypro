##########################################
import io
import sys

_INPUT = """\
7 3
2 0 2 3 2 1 9






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,K = map(int,input().split())
Alist = list(map(int,input().split()))
Alist = set(Alist)
ans = -1
#print (Alist)
for i in range(K):
    #print (i)
    if i not in Alist:
        print(i)
        quit()
        
if ans==-1:
    print (K)
else:
    print (ans)