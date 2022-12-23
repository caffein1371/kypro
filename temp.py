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
for i in range(K):
    if A>=B:
        B = 2*B
    elif B>=C:
        C = 2*C
if A<B<C:
    print ("Yes")
else:
    print ("No")
#print (A,B,C)