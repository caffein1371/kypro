##########################################
import io
import sys

_INPUT = """\
12
100 104 102 105 103 103 101 105 104 102 104 101



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
A = list(map(int,input().split()))
#累積和の問題？
ans = float('Inf')
temp = [0 for i in range(N+1)]
for i in range(N):
    temp[i+1]= temp[i]+A[i]
temp1 = [0 for i in range(N+1)]
#print (temp)
B = A[::-1]
for i in range(N):
    temp1[i+1] = temp1[i]+B[i]
temp1 = temp1[::-1]
#print (temp1)

for i in range(0,N):
    ans = min(ans,abs(temp1[i+1]-temp[i+1]))
print (ans)