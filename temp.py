##########################################
import io
import sys

_INPUT = """\
0 3 1 5











"""
sys.stdin = io.StringIO(_INPUT)
##########################################
L1,R1,L2,R2 = map(int,input().split())
L = max(L1,L2)
R = min(R1,R2)
if R1<L2 or R2<L1:
    print (0)
else:
    print (abs(L-R))