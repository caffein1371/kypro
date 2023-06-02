##########################################
import io
import sys

_INPUT = """\
30 10 20
11 13
30 14
6 4
7 23
30 8
17 4
6 23
24 18
26 25
9 3
18 4 36 46 28 16 34 19 37 23 25 7 24 16 17 41 24 38 6 29 10 33 38 25 47 8 13 8 42 40
2 1 9
1 8
1 9
2 20 24
2 26 18
1 20
1 26
2 24 31
1 4
2 21 27
1 25
1 29
2 10 14
2 2 19
2 15 36
2 28 6
2 13 5
1 12
1 11
2 14 43



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,M,Q = map(int,input().split())
G = [[]for i in range(N)]
for i in range(M):
    u,v = map(int,input().split())
    u-=1
    v-=1
    G[u].append(v)
    G[v].append(u)

#初期状態の色
col = list(map(int,input().split()))

for i in range(Q):
    t,x,*y = map(int,input().split())
    x-=1
    print (col[x])
    if t==1:
        for i in G[x]:
            col[i] = col[x]
    elif t==2:
        col[x] = y[0]