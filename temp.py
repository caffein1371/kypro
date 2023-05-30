##########################################
import io
import sys

_INPUT = """\
103



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
X = int(input())

result= 100
n=0
while(result<X):
    result =  result+result//100
    #print (result)
    n+=1
print (n)