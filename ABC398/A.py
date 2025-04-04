##########################################
import io
import sys

_INPUT = """\
10


"""
sys.stdin = io.StringIO(_INPUT)
##########################################

N = int(input())

temp = []
if N%2!=0:
    for i in range(N//2):
        temp.append('-')
    temp.append('=')
    for i in range(N//2):
        temp.append('-')
else:
    for i in range(N//2-1):
        temp.append('-')
    #print (temp)
    temp.append('=')
    l_reversed = reversed(temp)
    temp.extend(l_reversed)

ans = ''.join(temp)
    
print (ans)

    