##########################################
import io
import sys

_INPUT = """\
4 3
8 5 -1 3
3 -2 -4



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N,M =  map(int,input().split())
Blist = sorted(list(map(int,input().split())),reverse=True)
Wlist = sorted(list(map(int,input().split())),reverse=True)
print (Blist)
print (Wlist)

ans0 = 0
ans1 = 1
temp = 0
for i in range(N):
    if Blist[i]>=0:
        ans0+=Blist[i]
        temp = i
    else:
        ans1=ans0+Blist[i]
        break
    
print (ans0)
print (ans1)

for i in range(temp):
    if Wlist[i]>=0:
        ans0+=Wlist[i]

print (max(ans0,ans1))