##########################################
import io
import sys

_INPUT = """\
314159265 358979323 84



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B,K = map(int,input().split())

for i in range(K):
    if i%2==0:
        if A%2!=0:
            A-=1
        #print (A,B)
        A=A//2
        temp=A
        B+=temp
        #print (A,B)
            
    elif i%2==1:
        if B%2!=0:
            B-=1
        B=B//2
        temp=B
        A+=temp

print (A,B)
    