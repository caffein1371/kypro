##########################################
import io
import sys

_INPUT = """\
2 10
20 20










"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,x = map(int,input().split())
Alist = list(map(int,input().split()))
Alist = list(sorted(Alist))
temp = 0
ans=0
Blist = []
if sum(Alist)<x:
        print (N-1)
        quit()

for i in range(len(Alist)):
        if temp+Alist[i]<=x:
                temp+=Alist[i]
                ans+=1
        else:
                break
print (ans)


