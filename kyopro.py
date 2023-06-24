##########################################
import io
import sys

_INPUT = """\
3
14159 26535 89793 23846 26433 83279 50288 41971 69399 37510 58209 74944 59230 78164 6286 20899 86280 34825 34211 70679 82148



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
A = list(map(int,input().split()))

ans = []
temp = len(A)
temp1 = len(A)//7

for i in range(temp1):
    ans1=0
    for i in range(i*7,(i+1)*7):
        ans1+=A[i]
    if i==temp1-1:
        print (ans1)
    else:
        print (ans1,end=' ')