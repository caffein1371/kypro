##########################################
import io
import sys

_INPUT = """\
3 5
#.#..
.....
.#...
2 2
#.
.#
5 3
...
#.#
.#.
.#.
...


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
import itertools
S = []
for i in range(N):
    s = input()
    S.append(s)

for i in itertools.permutations(S,2):
    #print (i)
    temp = ''.join(i)
    #print(temp)
    M = len(temp)
    flag=[]
    for j in range(M):
        if temp[j]==temp[M-1-j] :
            flag.append(True)
    if sum(flag)==M:
        print ('Yes')
        exit()
print ('No')


