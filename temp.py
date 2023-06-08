##########################################
import io
import sys

_INPUT = """\
5
10 20 30 40 50


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))
temp = [0 for i in range(N+1)]
for i in range(N):
    temp[i+1]=Alist[i]+temp[i]
#print (temp)

for i in range(1,N+1):
    ans = 0
    for j in range(N-i+1):
        diff = temp[j+i]-temp[j]
        ans = max(diff,ans)
    print (ans)

