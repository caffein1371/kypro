##########################################
import io
import sys

_INPUT = """\
20 1 30
1 10





"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,M,T = map(int,input().split())
AB = []
temp = 0
ans = N
for i in range(M):
    A,B = map(int,input().split())
    ans = ans-(A-temp)
    if ans<=0:
        print ('No')
        quit()
    if ans+(B-A)>=N:
        ans = N
    else:
        ans = ans+(B-A)
    temp = B

ans = ans-(T-temp)
if ans<=0:
    print ('No')
else:
    print ('Yes')
