##########################################
import io
import sys

_INPUT = """\
4 1 10
10 7 5
2 10






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,M,T = map(int,input().split())
Alist = list(map(int,input().split()))
X = []
Y = []
for i in range(M):
    x,y = map(int,input().split())
    Alist[x-1]-=y

for i in range(len(Alist)):
    T-=Alist[i]

if T<=0:
    print ("No")
else:
    print ("Yes")