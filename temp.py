##########################################
import io
import sys

_INPUT = """\
CODEFESTIVAL2014




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
S = input()
print (S.replace('2014','2015'))

