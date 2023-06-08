##########################################
import io
import sys

_INPUT = """\
6 3
2 0 2 -1 0 -4


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,K = map(int,input().split())
Alist = list(map(int,input().split()))
temp = [0 for i in range(N+1)]
for i in range(N):
    temp[i+1]=Alist[i]+temp[i]
#print (temp)

for i in range(N-K+1):
    diff = temp[i+K]-temp[i]
    print (diff)

