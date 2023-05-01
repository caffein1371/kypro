##########################################
import io
import sys

_INPUT = """\
4 4
.1.#
###.
.#2.
#.##






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
R,C =map(int,input().split())
B = []
for i in range(R):
    Blist = input()
    B.append(Blist)

ans = [['#' for i in range(C)] for j in range(R)]

for i in range(R):
    for j in range(C):
        #p = B[i][j]
        x =B[i][j]
        for s in range(R):
            for h in range(C):
                if B[s][h]!='#' and B[s][h]!='.':
                    p = int(B[s][h])
                else:
                    p = -1
                if abs(i-s)+abs(j-h)<=p:
                        x ='.'
        print (x,end='')
    print ()
        