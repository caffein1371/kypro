##########################################
import io
import sys

_INPUT = """\
9


"""
sys.stdin = io.StringIO(_INPUT)
##########################################


N = int(input())

ans = []
for i in range(N):
    if (i+1)%3==0:
        ans.append('x')
    else:
        ans.append('o')

print (''.join(ans))