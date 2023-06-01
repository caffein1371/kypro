##########################################
import io
import sys

_INPUT = """\
10
aabbbbaaca


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
S = input()
i = 0
ans = []
while i<len(S):
    j=i+1
    while j<len(S) and S[i]==S[j]:
        j+=1
    ans.append(S[i])
    i= j

print (len(ans))