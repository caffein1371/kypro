##########################################
import io
import sys

_INPUT = """\
........
........
........
........
........
.*......
........
........



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
yoko = ['a','b','c','d','e','f','g','h','i']
for i in range(8):
    S = input()
    if '*' in S:
        print (str(yoko[S.find('*')])+str(8-i))