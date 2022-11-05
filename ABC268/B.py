##########################################
import io
import sys

_INPUT = """\
abc
abc

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
S = input()
T = input()
#print (T[0:len(S)])
if S == T[:len(S)]:
    print ("Yes")
else:
    print ("No")
