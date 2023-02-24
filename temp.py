##########################################
import io
import sys

_INPUT = """\
9




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
print (10**N+7)