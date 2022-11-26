##########################################
import io
import sys

_INPUT = """\
3 4

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
X,Y = map(int,input().split())
import math
temp = math.sqrt(X**2+Y**2)
print(X/temp,Y/temp)