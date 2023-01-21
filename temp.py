##########################################
import io
import sys

_INPUT = """\
5 1 2
rrefa






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,A,B = map(int,input().split())
S = input()

from collections import deque
import collections

c = collections.Counter(S)
print (c)
