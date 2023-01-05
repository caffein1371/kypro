##########################################
import io
import sys

_INPUT = """\
abc











"""
sys.stdin = io.StringIO(_INPUT)
##########################################
S = input()
if len(S)%2==0:
    print (S)
else:
    print (S[::-1])

