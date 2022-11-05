##########################################
import io
import sys

_INPUT = """\
4
1 2 0 3

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
plist = list(map(int,input().split()))
