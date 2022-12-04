##########################################
import io
import sys

_INPUT = """\
Y
a



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
S = input()
T = input()
if S=="Y":
    print (T.upper())
else:
    print (T)