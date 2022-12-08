##########################################
import io
import sys

_INPUT = """\
4 11







"""
sys.stdin = io.StringIO(_INPUT)
##########################################
a,b = map(int,input().split())
if a+b==15:
    print ("+")
elif a*b==15:
    print ("*")
else:
    print ("x")


