##########################################
import io
import sys

_INPUT = """\
4
BRBR



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
s = input()
rc = s.count('R')
bc = s.count('B')
if rc>bc:
        print ('Yes')
else:
        print ('No')