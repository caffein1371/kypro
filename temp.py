##########################################
import io
import sys

_INPUT = """\
1222











"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = input()
print (N.count("2"))