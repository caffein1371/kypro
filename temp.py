##########################################
import io
import sys

_INPUT = """\
4
ooxx
xoox
xxxx
xxxx


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N= int(input())
S = []
for i in range(N):
    s = input()
    S.append(s)
ans = [["x" for j in range(N)]for i in range(N)]
for i in range(N):
    for j in range(N):
        ans[j][i]=S[N-1-i][j]

for i in range(N):
    a = ans[i]
    print ("".join(a))
