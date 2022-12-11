##########################################
import io
import sys

_INPUT = """\
15
13 76 46 15 50 98 93 77 31 43 84 90 6 24 14




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = [0]+list(map(int,input().split()))
#print(Alist)
ans=0
for i in range(1,len(Alist)):
    if i%2==1 and Alist[i]%2==1:
        ans+=1
print(ans)
