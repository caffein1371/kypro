##########################################
import io
import sys

_INPUT = """\
4
3
4
1
2



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
A = []

for i in range(N):
    a = int(input())
    A.append(a)
ans=0
cur = 1
flag = False
while ans<100001:
    #print (A[A[i]-1]==2)
    cur = A[cur-1]
    #print (cur)

    if cur==2:
        flag=True
        break
    ans+=1


if flag:
    print (ans+1)
else:
    print (-1)