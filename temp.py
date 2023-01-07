##########################################
import io
import sys

_INPUT = """\
2
3
8


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
a = int(input())
b = int(input())
n = int(input())

import math
temp = math.gcd(a,b)
ans = (a*b)/(temp) 

i=1
temp =ans
while ans<n:
    ans =ans*i
    i+=1
    if ans<n:
        ans = temp
    

print (int(ans))





