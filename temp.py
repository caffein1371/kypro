##########################################
import io
import sys

_INPUT = """\
2
1 0








"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))
Alist = list(set(Alist))
Alist = sorted(Alist,reverse=True)
ans= -1

gu = []
ki = []
for i in range(len(Alist)):
    if Alist[i]%2==0:
        ki.append(Alist[i])
    else:
        gu.append(Alist[i])
kis =-1
gus =-1
try:
    kis=ki[0]+ki[1]
except:
    pass
try :
    gus = gu[0]+gu[1]
except:
    pass

print (max(kis,gus))