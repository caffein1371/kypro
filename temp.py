##########################################
import io
import sys

_INPUT = """\
4
1 3 5 2
2 3 1 4


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N= int(input())
Alist = list(map(int,input().split()))
Blist = list(map(int,input().split()))

ans = 0
ans1 = 0
for i in range(N):
    if Alist[i]==Blist[i]:
        ans+=1
    if Alist[i] in Blist and Alist[i]!=Blist[i]:
        ans1+=1
print (ans)
print (ans1)