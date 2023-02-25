##########################################
import io
import sys

_INPUT = """\
4
unagi 20
usagi 13
snuke 42
smeke 7



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
d = dict()
temp = 0
for i in range(N):
    S,P = map(str,input().split())
    #data = (S,int(P))
    temp+= int(P)
    d[S]=int(P)
d = sorted(d.items(),key=lambda x:x[1],reverse=True)
#print (d)
#print (temp)
if d[0][1]>temp/2:
    print (d[0][0])
else:
    print ('atcoder')
