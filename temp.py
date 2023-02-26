##########################################
import io
import sys

_INPUT = """\
3 5





"""
sys.stdin = io.StringIO(_INPUT)
##########################################
R,D = map(int,input().split())
import math
print (R*R*math.pi*D*2*math.pi)