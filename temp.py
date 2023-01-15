##########################################
import io
import sys

_INPUT = """\
5
newfile
newfile
newfolder
newfile
newfolder




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
F = []
from collections import defaultdict
d = defaultdict(int)
for i in range(N):
    f = input()
    if d[f]==0:
        print (f)
    else:
        print (f+'('+str(d[f])+')')
    d[f]+=1
    
#print (d)