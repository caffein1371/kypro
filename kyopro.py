##########################################
import io
import sys

_INPUT = """\
1000000000000000000






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
from functools import lru_cache

@lru_cache(maxsize=None)
def func(n):
    if n<2:
        return 1
    elif n>=2:
        return n*(func(n-2))
N = int(input())
temp = func(N)
temp1 = str(temp)[::-1]
ans = 0
#print (temp1[0])
for i in range(len(temp1)):
    if temp1[i]=='0':
        ans+=1
    else:
        break
print (ans)