##########################################
import io
import sys

_INPUT = """\
7 2 5
3





"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B,C = map(int,input().split())
K = int(input())

A1 = A*2
B1 = B*2
C1 = C*2

if B1>A or C1>B:
    print ("Yes")
else:
    print ("No")