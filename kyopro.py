##########################################
import io
import sys

_INPUT = """\
2 3
0 1 2
0 0 3



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
H,W = map(int,input().split())
ABC = ['.','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
for i in range(H):
    Alist = list(map(int,input().split()))
    ans = []
    for j in range(W):
        ans.append(ABC[Alist[j]])
    print (''.join(ans))