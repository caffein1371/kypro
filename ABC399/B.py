##########################################
import io
import sys

_INPUT = """\
4
3 12 9 9


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
Plist = list(map(int,input().split()))

r = 1
rank = [i+1 for i in range(N)]
print (rank)
