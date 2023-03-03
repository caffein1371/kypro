##########################################
import io
import sys

_INPUT = """\
5
1 4 3 5 8




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Alist = list(map(int,input().split()))
Alist = sorted(Alist)
import itertools
ans = -1
#print (Alist[-3:])
for v in itertools.permutations(Alist[-3:],3):
    temp = int(''.join(str(v[0])+str(v[1])+str(v[2])))
    #print (temp)
    ans = max(temp,ans)
print (ans)