##########################################
import io
import sys

_INPUT = """\
1000





"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A = int(input())
import math
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN
temp = math.pow(A,1/3)
#print (temp)
ans = Decimal(str(temp)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
#print (Decimal(str(math.pow(A,1/3)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)))

if ans**3==A:
        print ('YES')
else:
        print ('NO')