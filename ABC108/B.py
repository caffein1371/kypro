##########################################
import io
import sys

_INPUT = """\
0 0 0 1




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
x1,y1,x2,y2 = map(int,input().split())
import math


x3=x1*math.cos(math.radians(-90))-y1*math.sin(math.radians(-90))+x2-x2*math.cos(math.radians(-90))+y2*math.sin(math.radians(-90))
y3=x1*math.sin(math.radians(-90))+y1*math.cos(math.radians(-90))+y2-x2*math.sin(math.radians(-90))-y2*math.cos(math.radians(-90))
x4=x2*math.cos(math.radians(90))-y2*math.sin(math.radians(90))+x1-x1*math.cos(math.radians(90))+y1*math.sin(math.radians(90))
y4=x2*math.sin(math.radians(90))+y2*math.cos(math.radians(90))+y1-x1*math.sin(math.radians(90))-y1*math.cos(math.radians(90))


print(int(x3),int(y3),int(x4),int(y4))