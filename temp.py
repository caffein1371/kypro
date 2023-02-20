##########################################
import io
import sys

_INPUT = """\
5 2 4
2
4
6
8
10






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,A,B = map(int,input().split())
#全体にPかけた場合，平均はP倍，最大ー最小はP倍
#全体にQを足した場合，平均はQ足され，最大ー最小は変わらない
#最大ー最小はP倍によって左右される
P = 0 
Q = 0
temp1 = 0
temp2 = 10**9
temp3 = 0
for i in range(N):
        s = int(input())
        temp1+=s
        temp2=min(temp2,s)
        temp3=max(temp3,s)
temp4 = temp3-temp2
if temp4==0:
        print (-1)
        quit()
P = B/temp4
Q = A-(temp1/N)*P

print (P,Q)