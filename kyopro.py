##########################################
import io
import sys

_INPUT = """\
5
1 2 3 5 6



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))
ans = []
for i in range(N):
    if Alist[i]%2==0:
        ans.append(Alist[i])
print (*ans)