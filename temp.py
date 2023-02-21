##########################################
import io
import sys

_INPUT = """\
99




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
# N = input()
# ans = 0
# if len(N)>1:
#         if N[0]!='9':
#                 ans+=int(N[0])-1
#                 ans+=len(N[1::])*9
#         if N[0]=='9' :
#                 ans+=8
#                 ans+=len(N[1::])*9
#         print (ans)
# else:
#         print (int(N))

N=int(input())
S=str(N)
c=0
for s in S:
  c+=int(s)
d=(len(S)-1)*9+int(S[0])-1
print(max(c,d))