##########################################
import io
import sys

_INPUT = """\
xxxxxxxx



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
S = input()
if S.count('x')>7:
        print ('NO')
else:
        print ('YES')