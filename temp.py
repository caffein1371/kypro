##########################################
import io
import sys

_INPUT = """\
4




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())

temp = 1
ans = []
for i in range(1,N):
    ans.append(i)

temp = ans.copy()

ans.append(N)
ans+=(temp[::-1])
print (ans)