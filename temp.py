##########################################
import io
import sys

_INPUT = """\
5 4
o--o
----
----
----
----









"""
sys.stdin = io.StringIO(_INPUT)
##########################################
H,W = map(int,input().split())
S = []
for i in range(H):
    s = input()
    for j in range(W):
        if s[j]=='o':
            r = j
            c = i
            S.append([c,r])
a,b = S[0]
c,d = S[1]
print (abs(a-c)+abs(b-d))

