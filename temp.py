##########################################
import io
import sys

_INPUT = """\
abaababaab


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
S = input()
import collections
#print (S)
flag = True

while flag:
    S =S[:-1]
    #print (S)
    #print (c)
    temp = len(S)//2
    if len(S)%2==0:
        if S[0:temp]==S[temp:len(S)]:
            flag=False
    
#print(S)
print (len(S))