##########################################
import io
import sys

_INPUT = """\
2000 20000000


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,Y = map(int,input().split())

c = 0
for i in range(N+1):
    for j in range(N+1):
        c = N-i-j
        if 10000*i+5000*j+1000*c ==Y and c>=0:
            print (i,j,c)
            exit()
print (-1,-1,-1)
