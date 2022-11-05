##########################################
import io
import sys

_INPUT = """\
31 9 24 31 24


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
anslist = list(map(int,input().split()))
print (len(set(anslist)))