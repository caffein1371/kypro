##########################################
import io
import sys

_INPUT = """\
4
0101
1101
1111
0000

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
from copy import deepcopy

N = int(input())
Alist = []
for i in range(N):
    A = list(input())
    Alist.append(A)
#print (Alist)
Blist = deepcopy(Alist)
#print (Blist)

for i in range(N-1):
    Blist[0][i+1]=Alist[0][i]
for i in range(N-1):
    Blist[i+1][N-1]=Alist[i][N-1]
for i in range(1,N):
    Blist[N-1][i-1]=Alist[N-1][i]
for i in range(1,N):
    Blist[i-1][0]=Alist[i][0]

for row in Blist:
    print("".join(map(str, row)))
