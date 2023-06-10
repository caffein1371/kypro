##########################################
import io
import sys

_INPUT = """\
2
3 1 2
6 1 1



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())

tempt,tempx,tempy = 0,0,0
for i in range(N):
    t,x,y = map(int,input().split())
    jikan = abs(t-tempt)
    xsa = abs(x-tempx)
    ysa = abs(y-tempy)
    if jikan<(xsa+ysa):
        #flag = False
        print ('No')
        exit()
    elif jikan%2==1 and (xsa+ysa)%2==0:
        print ('No')
        exit()
        #flag = False
    elif jikan%2==0 and (xsa+ysa)%2==1:
        print ('No')
        exit()
        # flag = False
    tempt,tempx,tempy=t,x,y
print ('Yes')
