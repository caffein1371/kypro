##########################################
import io
import sys

_INPUT = """\
7
50
30
50
100
50
80
30


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
D = []
for i in range(N):
    d = int(input())
    D.append(d)
D = set(D)
print (len(D))
