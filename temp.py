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

res = 0
right = 0 
sume = 0
for left in range(N):
    #print (left)
    while (right<N and sume+alist[right]<K):
        sume+=alist[right]
        right+=1
    
    #print (sume)
    res+=right-left
    if right==left:
        right+=1
    else:
        sume-=alist[left]

    #print (right)
print (res)