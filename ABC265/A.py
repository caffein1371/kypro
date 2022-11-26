##########################################
import io
import sys

_INPUT = """\
100 100 100





"""
sys.stdin = io.StringIO(_INPUT)
##########################################
X,Y,N = map(int,input().split())

ans = N*X
temp = N//3
print (min(temp*Y+(N-temp*3)*X,ans))