##########################################
import io
import sys

_INPUT = """\
1234567890







"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
import math

temp = int(math.sqrt(N))
print (temp)
temp1 = int(math.log2(N))
ans = 0
for i in range(2,temp+2):
    for j in range(2,temp+2):
        if temp1/(2*int(math.log2(i)))==j:
            ans+=1

print (ans)
