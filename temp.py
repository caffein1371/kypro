##########################################
import io
import sys

_INPUT = """\
5
4
2







"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
H = int(input())
W = int(input())

a = N-H+1
b = N-W+1

print (a*b)
