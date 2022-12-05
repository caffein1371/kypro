##########################################
import io
import sys

_INPUT = """\
3



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
temp = ["ACL" for i in range((N))]
print ("".join(temp))
