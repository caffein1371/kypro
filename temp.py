##########################################
import io
import sys

_INPUT = """\
34
ABABAAABACDDDABADFFABABDABFAAABFAA



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
S = input()
ans = 0
for i in range(N):
        if S[i]=='A':
                ans+=4
        elif S[i]=='B':
                ans+=3
        elif S[i]=='C':
                ans+=2
        elif S[i]=='D':
                ans+=1
print (float(ans/N))
