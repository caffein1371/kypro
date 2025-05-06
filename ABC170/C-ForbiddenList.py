##########################################
import io
import sys

_INPUT = """\
6 5
4 7 10 6 5


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
X,N = map(int,input().split())
plist = list(map(int,input().split()))
