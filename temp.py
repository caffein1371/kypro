##########################################
import io
import sys

_INPUT = """\
7
1 2 3 4 5 6


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))
G = [0 for i in range(N)]
for i in range(len(Alist)):
    G[Alist[i]-1]+=1

for i in range(N):
    print (G[i])