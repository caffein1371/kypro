##########################################
import io
import sys

_INPUT = """\
3
5 6
5 6 10










"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N= int(input())
A,B = map(int,input().split())
Plist = list(map(int,input().split()))
temp1 = 0
temp2 = 0
temp3 = 0
for i in Plist:
    if i<=A:
        temp1+=1
    if A+1<=i<=B:
        temp2+=1
    if B+1<=i:
        temp3+=1
temp = min(temp1,temp2,temp3)

print (temp)
