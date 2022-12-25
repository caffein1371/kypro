##########################################
import io
import sys

_INPUT = """\
2 3









"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,M = map(int,input().split())
import itertools
a = [i for i in range(1,M+1)]
 
for v in itertools.combinations(a,N):
    print (*v)