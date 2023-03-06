##########################################
import io
import sys

_INPUT = """\
B c



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
C,c = map(str,input().split())
if c.upper()==C:
    print ('Yes')
else:
    print ('No')