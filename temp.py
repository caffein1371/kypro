##########################################
import io
import sys

_INPUT = """\
100000 1
1 99999




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,M = map(int,input().split())
G = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)

#print (G)
for i in G[0]:
    #print (i)
    for j in G[i]:
        if j==N-1:
            print ('POSSIBLE')
            exit()

print ('IMPOSSIBLE')
