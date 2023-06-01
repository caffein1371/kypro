##########################################
import io
import sys

_INPUT = """\
5 2
1 1 2 2 5





"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,K = map(int,input().split())
Alist = list(map(int,input().split()))

ans = len(set(Alist))
if ans<=K:
    print (0)
    exit()

from collections import Counter

temp = Counter(Alist)

temp1 = dict(sorted(temp.items()))


i=0
Ans = 0
while ans>K:
    
    ans-=temp1[i].values()
    Ans+=temp[i].values()
    i+=1
print (Ans)