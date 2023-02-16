##########################################
import io
import sys

_INPUT = """\
10 1








"""
sys.stdin = io.StringIO(_INPUT)
##########################################
t,N= map(int,input().split())
ans = []
import decimal
ans = 0
for i in range(1,t+1):
    print (((t+100)//100)*i)