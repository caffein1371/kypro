##########################################
import io
import sys

_INPUT = """\




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
def func(n):
        if n==0 or n==1:
                return 100
        elif n==2:
                return 200
        else:
                return func(n-1)+func(n-2)+func(n-3)
print (func(19))