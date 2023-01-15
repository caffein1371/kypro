##########################################
import io
import sys

_INPUT = """\
6
abcbac


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
S = input()
j = 0
l = 0
temp=0
from collections import defaultdict
d = defaultdict(list)
for i in range(N):
    for j in range(i+1,N):
        #print (i,j,S[i],S[j])
        d[abs(i-j)].append([S[i],S[j]])
#print (d)
l = 0
for v in range(1,len(d)+1):
    l = 0
    for i in range(len(d[v])):
        #print (d[v][i])
        if d[v][i][0]!=d[v][i][1]:
            l+=1
        else:
            break
    print (l)