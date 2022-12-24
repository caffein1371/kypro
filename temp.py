##########################################
import io
import sys

_INPUT = """\
2 2
.#
#.





"""
sys.stdin = io.StringIO(_INPUT)
##########################################
H,W = map(int,input().split())
S = []
ans = 0
for i in range(H):
    s = input()
    S.append(s)
    for i in range(1,W):
        if s[i]=="." and s[i-1]==".":
            ans+=1
#print (S)
temp =[["" for i in range(H)] for j in range(W)]
for i in range(len(S)):
    for j in range(len(S[i])):
        temp[j][i]= S[i][j]
for i in range(len(temp)):
    #print (temp[i])
    for j in range(1,len(temp[i])):
        if temp[i][j]=="." and temp[i][j-1]==".":
            ans+=1

print (ans)