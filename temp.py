##########################################
import io
import sys

_INPUT = """\
12
18
11







"""
sys.stdin = io.StringIO(_INPUT)
##########################################
A = int(input())
B = int(input())
C = int(input())

if A>B>C:
  print (1)
  print (2)
  print (3)
elif A>C>B:
  print (1)
  print (3)
  print (2)
elif B>A>C:
  print (2)
  print (1)
  print (3)
elif B>C>A:
  print (3)
  print (1)
  print (2)
elif C>A>B:
  print (2)
  print (3)
  print (1)
elif C>B>A:
  print (3)
  print (2)
  print (1)



