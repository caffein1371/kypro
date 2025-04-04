##########################################
import io
import sys

_INPUT = """\
3 4






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B = map(int,input().split())

a = [[1,2,3], [4,5,6],[7,8,9]]

for i in range(3):
    #print (a[i])
    if A in a[i] and B in a[i]:
        print ('Yes')
        exit()


print ('No')
