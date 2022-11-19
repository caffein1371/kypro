##########################################
import io
import sys

_INPUT = """\
2 8
1 1 2
1 2 1
3 1 2
1 1 2
1 1 2
1 1 2
2 1 2
3 1 2




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,Q = map(int,input().split())
from collections import defaultdict

d = defaultdict(list)
for i in range(Q):
    T,A,B = map(int,input().split())
    if T==1:
        d[A].append(B)
    if T==2:
        try:
            d[A].remove(B)
        except:
            pass
    if T==3:
        # d[A]=list(set(d[A]))
        # d[B]=list(set(d[B]))
        if B in d[A] and A in d[B]:
            print ("Yes")
        else:
            print ("No")
    #print(d)

