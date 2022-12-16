##########################################
import io
import sys

_INPUT = """\
11 30
12 1














"""
sys.stdin = io.StringIO(_INPUT)
##########################################
M1,D1 = map(int,input().split())
M2,D2 = map(int,input().split())
if (abs(M2-M1)==1 or abs(M2-M1)==11) and abs(D1-D2)>1:
    print (1)
else:
    print (0) 
