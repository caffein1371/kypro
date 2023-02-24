##########################################
import io
import sys

_INPUT = """\
5
4 2 5 1 3






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Plist = list(map(int,input().split()))
temp = float('inf')
ans = 0
for i in Plist:
  if i < temp:
    temp = i
    ans += 1
print (ans)