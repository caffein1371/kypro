##########################################
import io
import sys

_INPUT = """\
3 500
1




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
x,y = map(int,input().split())
k = int(input())
if y>k:
        temp = y-k
        x+=k
        print (x)
        
elif k>=y:
        temp = k-y
        x+=y
        x-=temp
        print (x)
