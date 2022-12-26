##########################################
import io
import sys

_INPUT = """\
500




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
ans = []
count = 10
while N!=0:
    if N>2**count:
        N = N%2**count
        ans.append(2**count)
    elif N==2:
        N = N%2
        ans.append(2)
    elif N==1:
        N = N%1
        ans.append(1)
    #print (N)
    count-=1

print (len(ans))
for i in ans:
    print (i)