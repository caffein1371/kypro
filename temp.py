##########################################
import io
import sys

_INPUT = """\
aabbbbbbbbbbbbxyza


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
S = input()
i = 0
ans = []
while i<len(S):
    j=i+1
    while j<len(S) and S[i]==S[j]:
        j+=1
    ans.append(S[i]+str(j-i))
    i= j
print (''.join(ans))
#print (len(ans))