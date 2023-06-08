##########################################
import io
import sys

_INPUT = """\
5 3 4



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B,N = map(int,input().split())

ans = (A*N//B)-A*(N//B)
if B-1<=N:
    ans = (A*(B-1)//B)-A*((B-1)//B)


print (ans)