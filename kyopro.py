##########################################
import io
import sys

_INPUT = """\
1000000000000000 1 1000000000000000





"""
sys.stdin = io.StringIO(_INPUT)
##########################################
Alist = list(map(int,input().split()))
#Alist = list(sorted(Alist))
X =2*Alist[1]-Alist[0]-Alist[2]
k = max(0,((1-X)//2))
print (X+3*k)
