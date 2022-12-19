##########################################
import io
import sys

_INPUT = """\
2 3
RDU
LRU









"""
sys.stdin = io.StringIO(_INPUT)
##########################################
H,W = map(int,input().split())
G = []
c,r=0,0
for i in range(H):
    g = input()
    G.append(g)
while True:
    if G[c][r]=="U" and c!=0:
        c-=1
    elif G[c][r]=="D" and c!=H-1:
        c+=1
    elif G[c][r]=="L" and r!=0:
        r-=1
    elif G[c][r]=="R" and r!=W-1:
        r+=1
    else:
        break

print (c+1,r+1)