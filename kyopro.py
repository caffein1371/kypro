##########################################
import io
import sys

_INPUT = """\
4 3
..#
...
.#.
...
#..
...
.#.
...



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
H,W = map(int,input().split())
A = []
ansA = []
for i in range(H):
    Alist = input()
    ans = 0
    for j in range(W):
        if Alist[j]=='#':
            ans+=1
    ansA.append(ans)
    A.append(Alist)
#print (A)
#print (ansA)
ansA1 = []
for i in range(W):
    ans=0
    for j in range(H):
        if A[j][i]=='#':
            ans+=1
    ansA1.append(ans)
#print (ansA1)
ansB = []
B = []
for i in range(H):
    Blist = input()
    ans = 0
    for j in range(W):
        if Blist[j]=='#':
            ans+=1
    ansB.append(ans)
    B.append(Blist)
ansB1 = []
for i in range(W):
    ans=0
    for j in range(H):
        if B[j][i]=='#':
            ans+=1
    ansB1.append(ans)
#print (ansB1)


#print (B)
#print (ansB)
if sorted(ansA)==sorted(ansB) or sorted(ansA1)==sorted(ansB1):
    print ('Yes')
else:
    print ('No')
