##########################################
import io
import sys

_INPUT = """\
10
1 8 4 15 7 5 7 5 8 0
20
2 7 0
3 7
3 8
1 7
3 3
2 4 4
2 4 9
2 10 5
1 10
2 4 2
1 10
2 3 1
2 8 11
2 3 14
2 1 9
3 8
3 8
3 1
2 6 5
3 7




"""
sys.stdin = io.StringIO(_INPUT)
##########################################


N = int(input())
Alist = list(map(int,input().split()))
Q = int(input())
for i in range(Q):
    qlist = list(map(int,input().split()))
    if qlist[0]==1:
        Alist = [qlist[1] for i in range(N)]
    elif qlist[0]==2:
        Alist[qlist[1]-1]+=qlist[2]
    elif qlist[0]==3:
        print (Alist[qlist[1]-1])

