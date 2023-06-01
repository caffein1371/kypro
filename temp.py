##########################################
import io
import sys

_INPUT = """\
4
3 3 3 3


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
b = list(map(int,input().split()))

from collections import Counter

temp = Counter(b)
temp = dict(temp)
#print (temp)
temp[0]=0
ans = 0
for key,value in temp.items():
    #print (key)
    #print (value)
    if key>value:
        ans+=value
    elif key<value:
        ans+=value-key

print (ans)