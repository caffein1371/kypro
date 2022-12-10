##########################################
import io
import sys

_INPUT = """\
1 1 1




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B,C = map(int,input().split())

if A+B==C and A-B==C:
    print ("?")
elif A+B==C and A-B!=C:
    print ("+")
elif A+B!=C and A-B==C:
    print ("-")
elif A+B!=C and A-B!=C:
    print ("!")
