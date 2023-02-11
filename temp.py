##########################################
import io
import sys

_INPUT = """\
4


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
from functools import lru_cache
@lru_cache(maxsize=None)

def S(n):
    if n==1:
        return [1]
    else:
        return S(n-1)+[n]+S(n-1)

N = int(input())
print (*S(N))