##########################################
import io
import sys

_INPUT = """\
999983







"""
sys.stdin = io.StringIO(_INPUT)
##########################################
K = int(input())
ans = []
answer = 0
temp1= 0
while len(ans)<12:
    ans.append('7')
    temp = int(''.join(ans))
    temp1+=temp
    print (temp)
    if temp%K==0:
        break

print (len(ans))