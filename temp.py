##########################################
import io
import sys

_INPUT = """\
111100





"""
sys.stdin = io.StringIO(_INPUT)
##########################################
S = input()
print (S.count("1"))