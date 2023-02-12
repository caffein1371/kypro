##########################################
import io
import sys

_INPUT = """\
10 6
1 2 3 7 8 9



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,M = map(int,input().split())
Alist = list(map(int,input().split()))
tmp = [i for i in range(1,N+1)]
if M==0:
    print (*tmp)
    quit()

flag = False

ans = [0]
for i in range(N):
    if i+1 not in Alist:
        #レ点がついていないもの
        ans.append(i+1)

print (*ans)
for i in range(len(ans)-1):
    for j in range(ans[i+1]-ans[i]):
        print (ans[i+1]-j,end=' ')

    