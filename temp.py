##########################################
import io
import sys

_INPUT = """\
4 10
6 1 2 7




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,K = map(int,input().split())
alist = list(map(int,input().split()))
temp = [0]+alist
for i in range(1,N+1):
    temp[i]+=temp[i-1]
print (temp)