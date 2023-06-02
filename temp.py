##########################################
import io
import sys

_INPUT = """\
4 3
1 2 3 4
1 3
2 3
2 4



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,M = map(int,input().split())
Hlist = list(map(int,input().split()))
G = [[]for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)
ans = 0
for i in range(N):
    # print (G[i])
    maxhigh=0
    if len(G[i])>0:
        for v in G[i]:
            maxhigh = max(Hlist[v],maxhigh)
        if maxhigh<Hlist[i]:
            ans+=1
    #     for v in G[i]:
    #         print (v)
    #         # if G[v]>=max(v):
    #             # ans+=1
    else:
        ans+=1
print (ans)