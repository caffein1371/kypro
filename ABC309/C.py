##########################################
import io
import sys

_INPUT = """\
4 4
6 3
2 5
1 9
4 2



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,K = map(int,input().split())
from collections import OrderedDict
d = {}
for i in range(N):
    a,b= map(int,input().split())
    d[a]=b
sd = OrderedDict(sorted(d.items()))
#print (sd)
temp = sum(sd.values())
#print (temp)

temp1 = 0
if temp<=K:
    print (1)
else:
    for i in sd.items():
        if temp<=K:
            print (temp1+1)
            exit()
        else:
            temp=temp-i[1]
        temp1 = i[0] 
    print (temp1+1)

