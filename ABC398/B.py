##########################################
import io
import sys

_INPUT = """\
13 13 1 1 7 4 13




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
import collections

Alist = list(map(int,input().split()))
c = collections.Counter(Alist)
#print (sorted(c.items(),reverse=True))
temp = list(sorted(c.values(),reverse=True))
#print (len(temp))
if len(temp)==1:
    print ('No')
    quit()

for i in range(len(temp)-1):
    if temp[i]>=3 and temp[i+1]>=2:
        print ('Yes')
        quit()
print ('No')