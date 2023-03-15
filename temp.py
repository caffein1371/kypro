##########################################
import io
import sys

_INPUT = """\
P



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
c = input()
ans = ['O','P','L','K']
if c in ans:
        print ('Right')
else:
        print ('Left')