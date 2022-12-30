##########################################
import io
import sys

_INPUT = """\
5
error
2



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
S = input()
K = int(input())

temp = S[K-1]
ans = []
for i in range(len(S)):
    if S[i]!=temp:
        ans.append("*")
    else:
        ans.append(S[i])
print ("".join(ans))