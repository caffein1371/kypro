##########################################
import io
import sys

_INPUT = """\
10 6 9
1 3 5 7 8 9
1 2 3 4 5 6 5 6 2





"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,K,Q =map(int,input().split())
Alist = list(map(int,input().split()))
List = list(map(int,input().split()))
for i in range(Q):
        if Alist[List[i]-1]+1<=N and Alist[List[i]-1]+1 not in Alist:
                Alist[List[i]-1]+=1

print (*Alist)
