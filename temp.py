##########################################
import io
import sys

_INPUT = """\
2 3 4







"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,X,Y = map(int,input().split())
dp = [False for i in range(N)]
     
