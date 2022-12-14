##########################################
import io
import sys

_INPUT = """\
0 3 3 7





"""
sys.stdin = io.StringIO(_INPUT)
##########################################
L1,R1,L2,R2 = map(int,input().split())

if R1<L2 or R2<L1:
    print (0)
elif L1<=L2 and R1<=R2:
    print (R1-L2)
elif L2<=L1 and R2<=R1:
    print (R2-L1)
elif L2<R1:
    print (abs(L2-R1))
elif R2<L1:
    print (abs(L1-R2))
