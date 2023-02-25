##########################################
import io
import sys

_INPUT = """\
9
a
b
c
c
b
c
b
d
e




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
import collections
ans = []
for i in range(N):
    S = input()
    ans.append(S)
c = collections.Counter(ans)
print(c.most_common()[0][0])