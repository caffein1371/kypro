##########################################
import io
import sys

_INPUT = """\
4 2 3 1
RUDL
-1 -1
1 0




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,M,H,K = map(int,input().split())
S = input()
X,Y = 0,0
xy = []
for i in range(M):
    x,y = map(int,input().split())
    xy.append([x,y])
xy = set(map(tuple, xy))
#print (xy)

for i in range(N):
    if H-1>=0:
        H-=1
    else:
        print ('No')
        quit()
    if S[i]=='R':
        X+=1
    elif S[i]=='L':
        X-=1
    elif S[i]=='U':
        Y+=1
    elif S[i]=='D':
        Y-=1

    if H<K:
        if(X,Y)in xy:
            H=K
            xy.remove((X,Y))

#xy = list(set(xy))
#print (xy)

print ('Yes')
