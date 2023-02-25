##########################################
import io
import sys

_INPUT = """\
1000000000 1000000000 1000000000





"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B,C = map(int,input().split())
print (A*B*C%(10**9+7))