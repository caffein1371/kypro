##########################################
import io
import sys

_INPUT = """\
1
F






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
S = input()
flag = True
for i in range(len(S)-1):
    if ((S[i]==S[i+1])==True):
        print ('No')
        quit()

print ('Yes')

        