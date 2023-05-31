##########################################
import io
import sys

_INPUT = """\
5 15


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
K,S = map(int,input().split())

z = 0
ans = 0
for i in range(K+1):
    for j in range(K+1):
        z = S-i-j
        if i+j+z==S and z>=0 and z<=K:
            ans+=1
            #print (i,j,z)
print (ans)

