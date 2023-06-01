##########################################
import io
import sys

_INPUT = """\
7
beat
vet
beet
bed
vet
bet
beet




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
S = []

for i in range(N):
    s = input()
    s = ''.join(s)
    S.append(s)
from collections import Counter
temp = Counter(S)
c = Counter(S)
values, counts = zip(*c.most_common())
maxcount = counts[0]

#print (maxans)
temp = sorted(dict(temp).items())
#print (temp)
for i in range(len(temp)):
    if maxcount==temp[i][1]:
        print (temp[i][0])