##########################################
import io
import sys

_INPUT = """\
3
1 2 3





"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N  = int(input())
wlist = list(map(int,input().split()))

sumans = sum(wlist)
ans = 0
temp = sumans
for i in range(N):
  ans += wlist[i]
  if abs(ans-(sumans-ans))>temp:
    break
  temp = abs(ans-(sumans-ans))
    
print (temp)