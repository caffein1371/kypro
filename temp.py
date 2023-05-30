##########################################
import io
import sys

_INPUT = """\
6 5
3 1 4 1 5 9



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,X = map(int,input().split())
Alist = list(map(int,input().split()))
A=set(Alist)

for i in A:
    if i - X in A:
        print ('Yes')
        exit()


print ('No')