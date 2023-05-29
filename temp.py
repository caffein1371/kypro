##########################################
import io
import sys

_INPUT = """\
-1 0 3






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A,B,C = map(int,input().split())
gu = True
if C%2!=0:
    gu = False
import math

if gu==True:
    if abs(B)==abs(A):
        print ('=')
    elif abs(A)>abs(B):
        print('>')
    elif abs(B)>abs(A):
        print ('<')
else:
    if A>=0 and B>=0:
        if abs(B)==abs(A):
            print ('=')
        elif abs(A)>abs(B):
            print('>')
        elif abs(B)>abs(A):
            print ('<')
    elif A>=0 and B<0:
        print ('>')
    elif A<0 and B>=0:
        print ('<')
    elif A<0 and B<0:
        if abs(B)==abs(A):
            print ('=')
        elif abs(A)<abs(B):
            print('>')
        elif abs(B)>abs(A):
            print ('<')