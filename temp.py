##########################################
import io
import sys

_INPUT = """\
5 10


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B = map(int,input().split())
print (max(A,B))
