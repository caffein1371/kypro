##########################################
import io
import sys

_INPUT = """\
4 3 2





"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,A,B = map(int,input().split())
tiles = [['-' for i in range(N+1)] for j in range(N+1)]
#print (tiles)
for i in range(N+1):
    if i%2==0:
        for j in range(N+1):
            if j%2==0:
                tiles[i][j]='.'
            else:
                tiles[i][j]='#'
    else:
        for j in range(N+1):
            if j%2==0:
                tiles[i][j]='#'
            else:
                tiles[i][j]='.'

print (tiles)


X = [['-' for i in range(A*N)] for j in range(B*N)]
print (X)
for i in range(A*N):
    for j in range(B*N):
        print (i,j)
        print (round(i/A),round(i/B))
        X[i][j]=tiles[round(i/A)][round(j/B)]

for i in range(A*N):
    print (''.join(X))
