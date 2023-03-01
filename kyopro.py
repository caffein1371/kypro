##########################################
import io
import sys

_INPUT = """\
20160123




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
print (N//25)