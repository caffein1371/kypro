##########################################
import io
import sys

_INPUT = """\
2 3 6 6


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
x1,y1,x2,y2 = map(int,input().split())
import math
temp = math.sqrt((x1-x2)**2+(y1-y2)**2)
x3=x2-temp
y3=y1+temp
x4=x1-temp
y4=y1

print (int(x3),int(y3),int(x4),int(y4))
