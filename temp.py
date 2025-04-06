##########################################
import io
import sys

_INPUT = """\
8
7 3 5 4 2 1 6 8
3 8 2 5 4 6 7 1



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
import itertools
Plist = tuple(list(map(int,input().split())))
Qlist = tuple(list(map(int,input().split())))
temp = [i for i in range(1,N+1)]
A = list(itertools.permutations(temp))


#print (A)
print (abs(A.index(Plist)-A.index(Qlist)))