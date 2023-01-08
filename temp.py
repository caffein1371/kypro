##########################################
import io
import sys

_INPUT = """\
3
2023
63
1059872604593911



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
T = int(input())
import math
for i in range(T):
    test = int(input())
    p,q = 0,0

    for j in range(2,int((test+1)**(1/3))+1):
        #print (int((test+1)**(1/3)))
        if test%j!=0:
            continue
        if (test/j)%j==0:
            p = j
            q = int (test/j/j)
        else:
            q = j
            p = int(math.sqrt(test/j))
        break
    print (p,q)

        







