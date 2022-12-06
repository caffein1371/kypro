##########################################
import io
import sys

_INPUT = """\
ZONeZONeZONe








"""
sys.stdin = io.StringIO(_INPUT)
##########################################
S = input()
print (S.count("ZONe"))



