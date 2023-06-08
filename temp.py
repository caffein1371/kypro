##########################################
import io
import sys

_INPUT = """\
8 3
ACACTACG
3 7
2 3
1 8




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,Q = map(int,input().split())
S = input()
temp = [0 for i in range(N+1)]
for i in range(1,N):
    temp[i+1]=temp[i]+(S[i-1:i+1]=='AC')
    #print (S[i-1:i+1]=='AC')


for i in range(Q):
    l,r = map(int,input().split())
    l-=1
    print (temp[r]-temp[l+1])