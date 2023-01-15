##########################################
import io
import sys

_INPUT = """\
ABBCCCDDDDEEEEEFFFFFF






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
S = input()
import collections
c = collections.Counter(S)

ans = ['A','B','C','D','E','F']
for i in range(len(ans)):
    if i!=len(ans)-1:
        print (c[ans[i]],end =' ')
    else:
        print (c[ans[i]])