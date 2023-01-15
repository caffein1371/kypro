##########################################
import io
import sys

_INPUT = """\
100 200 50 20
40 10




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B,C,K = map(int,input().split())
S,T = map(int,input().split())
temp = A*S+B*T
if S+T>=K:
    print (temp-(S+T)*C)
else:
    print (temp)