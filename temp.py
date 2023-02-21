##########################################
import io
import sys

_INPUT = """\
3 200
3 10 10 10
3 10 10 10
5 2 2 2 2 2



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,X = map(int,input().split())
Alist = []
for i in range(N):
        Llist = list(map(int,input().split()))
        Alist.append(Llist[1::])
print (Alist)
import itertools

for i in range(N):
        for v in itertools.combinations(Alist,1):