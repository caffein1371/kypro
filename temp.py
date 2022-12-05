##########################################
import io
import sys

_INPUT = """\
10 20 30 40




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B,C,D = map(int,input().split())
if B<C:
    print ("No")
elif D<A:
    print ("No")
else:
    print ("Yes")