##########################################
import io
import sys

_INPUT = """\
8
a(b(d))c



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
S = input()

from collections import deque


A = deque()
T = []
for i in range(len(S)):
    if S[i]!=')' and S[i]!='(':
        T.append(S[i])
    elif S[i]=='(':
        T.append(S[i])
        A.append(i)
    elif S[i]==')':
        if len(A)!=0:
            x = A.pop()
            T = T[0:x]
        else:
            T.append(S[i])
print (''.join(T))
