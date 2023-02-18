##########################################
import io
import sys

_INPUT = """\
-505 191 278





"""
sys.stdin = io.StringIO(_INPUT)
##########################################
a,b,d = map(int,input().split())
import math
# print (math.radians(d))

print (a*math.cos(math.radians(d))-b*math.sin(math.radians(d)),a*math.sin(math.radians(d))+b*math.cos(math.radians(d)))

# d = math.radians(d)
# print (d)
# ans1 = a*math.cos(d)-b*math.sin(d)
# ans2 = a*math.sin(d)+b*math.cos(d)
# print (ans1,ans2)

from math import sin, cos, radians

# a, b, d = map(int, input().split())
# d = radians(d)
# print(a * cos(d) - b * sin(d), a * sin(d) + b * cos(d))
