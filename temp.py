##########################################
import io
import sys

_INPUT = """\
6 6
3
2 3 6
3
2 4 6
2
3 6
3
1 5 6
3
1 3 6
2
1 4



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,M = map(int,input().split())
A = []
for i in range(M):
    c = int(input())
    alist = list(map(int,input().split()))
    A.append(alist)
#print (A)
an = 0
tmp =[]
for i in range(2**M):
    ans = []
    for j in range(M):
        #ans = []
        if ((i>>j)&1):
            #print (A[j])
            for k in A[j]:
                #print (k)
                ans.append(k)
            tmp = set(ans)
            #print (tmp)
            if len(tmp)==N:
                an+=1
                break
            #print ()
            tmp = []

print (an)


    