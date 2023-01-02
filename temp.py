##########################################
import io
import sys

_INPUT = """\
90 30






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
n,x = map(int,input().split())
temp = n//2
if temp<x:
    print (n-x)
else:
    print (x-1)