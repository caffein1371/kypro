##########################################
import io
import sys

_INPUT = """\
1 2 3 1




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B,C,K = map(int,input().split())

temp = A-B

if abs(temp)>10**18:
    print ('Unfair')
else:
    if K%2==0:
        print (temp)
    else:
        print ((-1)*(temp))

