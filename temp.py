##########################################
import io
import sys

_INPUT = """\
hihi


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
S = input()
if 'hi' in S:
        print ('Yes')
else:
        print ('No')