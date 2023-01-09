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
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
for i in range(T):
    N=int(input())
    
    #print (temp)
    
    for p in range(2,int(N**(1/3))+1):
        if N%p==0:
            q = N//p
            if q%p==0:
                print (p,N//(p**2))
                break
            else:
                print (int(math.sqrt(q)),p)
                break

        







