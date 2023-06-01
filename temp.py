##########################################
import io
import sys

_INPUT = """\
4
2
5
5
2




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())

temp = set()
for i in range(N):
    A = int(input())
    if A in temp: 
        temp.remove(A)
    else:
        temp.add(A)
print (len(temp))