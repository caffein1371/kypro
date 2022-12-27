##########################################
import io
import sys

_INPUT = """\
10 2 4








"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B,C = map(int,input().split())
if A<C<B or A>C>B:
    print ("Yes")
else:
    print ("No")