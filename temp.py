##########################################
import io
import sys

_INPUT = """\
5 50 100
120
-10
-20
-30
70





"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,S,T = map(int,input().split())
W = int(input())
A = []
ans = 0
if S<=W<=T:
    ans+=1

for i in range(N-1):
    a = int(input())
    W = W+a
    if S<=W<=T:
        ans+=1
    if W<0:
        W = 0
print (ans)