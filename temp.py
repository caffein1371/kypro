##########################################
import io
import sys

_INPUT = """\
1
o
0


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
S = input()
T = input()

flag = True
for i in range(N):
    #print (S[i])
    #print (T[i])
    if (S[i]==T[i]) or (S[i]=='1' and T[i]=='l') or (S[i]=='0' and T[i]=='o') or (S[i]=='l' and T[i]=='1') or (S[i]=='o' and T[i]=='0'):
        #flag = True
        pass
    else:
        flag = False
        break

if flag:
    print ('Yes')
else:
    print ('No')