##########################################
import io
import sys

_INPUT = """\
1355506027









"""
sys.stdin = io.StringIO(_INPUT)
##########################################
S = input()
#print (len(S))
temp = S.count("00")
print (len(S)-temp)