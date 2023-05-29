##########################################
import io
import sys

_INPUT = """\
4
2 5 1 2














"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))
ans = []
for i in range(N-1):
    if Alist[i]-Alist[i+1]<-1:
        for j in range(Alist[i],Alist[i+1],1):
            ans.append(j)
            #print (j)
    elif Alist[i]-Alist[i+1]>1:
        for j in range(Alist[i],Alist[i+1],-1):
            ans.append(j)
            #print (j)

    elif abs(Alist[i]-Alist[i+1])==1:
        ans.append(Alist[i])

ans.append(Alist[-1])
print (*ans)