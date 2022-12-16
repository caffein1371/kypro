##########################################
import io
import sys

_INPUT = """\
1079
















"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
import math

for i in range(1,50001):
    
    if math.floor(i*1.08)== N:
        #print ((math.floor(i*1.08)))
        print (i)
        quit()
print (":(")