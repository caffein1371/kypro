##########################################
import io
import sys

_INPUT = """\
abcdef
2
3 5
1 4






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
S = list(input())
N = int(input())
LR = []
import copy
temp = copy.copy(S)
for i in range(N):
    l,r = map(int,input().split())
    a = temp[l-1:r][::-1]
    #print (a)
    temp[l-1:r]=a
    #print ("".join(temp)) 

    
print ("".join(temp)) 



