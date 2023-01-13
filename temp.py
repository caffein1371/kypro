##########################################
import io
import sys

_INPUT = """\
17






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
L = int(input())
ans = 1
from scipy.special import comb

print (comb(L-1,11,True))
