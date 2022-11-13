##########################################
import io
import sys

_INPUT = """\
4
2 4
4 3
4 10
8 1


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
from collections import defaultdict,deque
d1 = defaultdict(list)

N = int(input())
for i in range(N):
    A,B = map(int,input().split())
    d1[A].append(B)
    d1[B].append(A)

que = deque()
que.append(1)
S = {1}
while que:
    v = que.popleft()
    #print(v)
    for i in d1[v]:
        #print(i)
        if not i in S:
            que.append(i)
            S.add(i)
print (max(S))

