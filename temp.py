##########################################
import io
import sys

_INPUT = """\
20




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
from math import isqrt

# a = 0
# for i in range(1000):
#     if 2**i>=10**18:
#         #aは最大でも60
#         a = i
#         break
# aは最大でも60
# print (a)

ans = 0
for i in range(1,61):
    ans+= (isqrt(N//(2**i))+1)//2
print (ans)


