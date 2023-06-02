##########################################
import io
import sys

_INPUT = """\
14
1 2 2 3 3 3 4 4 4 4 1 2 3 4





"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
S =list(map(int,input().split()))
i=0
Ans = 0
while i<len(S):
    j=i+1
    ans = 1
    #同じ色に並んでいる区間の長さを求める
    while j<len(S) and S[i]==S[j]:
        ans+=1
        j+=1
    Ans+=ans//2
    i=j
    
print (Ans)