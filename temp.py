##########################################
import io
import sys

_INPUT = """\
2 1



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
#2<=N<=5,1<=M<=N
N,M = map(int,input().split())
for i in range(1,N+1):
        if i!=M:
                print (i)
                exit()
