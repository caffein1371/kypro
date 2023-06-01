##########################################
import io
import sys

_INPUT = """\
5 5
4 2 3 4 5
4 1 3 4 5
4 1 2 4 5
4 1 2 3 5
4 1 2 3 4




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,M = map(int,input().split())

ans = [i for i in range(1,31)]
ans = set(ans)
#print (ans)
for i in range(N):
    Kalist = list(map(int,input().split()))
    alist = set(Kalist[1:])
    ans = ans & alist
print (len(ans))