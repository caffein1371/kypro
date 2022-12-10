##########################################
import io
import sys

_INPUT = """\
1000 1 1








"""
sys.stdin = io.StringIO(_INPUT)
##########################################
X,Y,Z = map(int,input().split())
ans = 10**6
while True:
    if ans/Z<Y/X:
        print (ans)
        break
    ans-=1

