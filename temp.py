##########################################
import io
import sys

_INPUT = """\
3
2 4 3





"""
sys.stdin = io.StringIO(_INPUT)
##########################################
S=input()
print(S.replace("HAGIYA","HAGIXILE"))
