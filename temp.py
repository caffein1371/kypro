##########################################
import io
import sys

_INPUT = """\
10 1










"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B = map(int,input().split())
from decimal import Decimal, ROUND_HALF_UP
#temp = round((2*B/A)**(-2/3)-1)
temp = Decimal((2*B/A)**(-2/3)-1).quantize(Decimal('1'), rounding=ROUND_HALF_UP) 
#print (temp)
import math
if math.sqrt(temp+1)!=0:
    #print ((B*temp)+A/math.sqrt(temp+1))
    print (Decimal((B*temp)+A/math.sqrt(temp+1)).quantize(Decimal('0.00000001'), rounding=ROUND_HALF_UP))
else:
    print (A)