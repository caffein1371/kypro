##########################################
import io
import sys

_INPUT = """\
5
10 4 8 7 3



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Hlist = list(map(int,input().split()))
i = 0
maxans = 0
ans = 0
while i<len(Hlist):
    j = i+1
    if j<len(Hlist) and Hlist[i]>=Hlist[j]:
        #print (Hlist[i])
        #j=j+1
        ans=ans+1
    else:
        ans=0
    maxans = max(ans,maxans)
    # print (i)
    # print (j)
    i=j
print (maxans)