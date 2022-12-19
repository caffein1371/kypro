##########################################
import io
import sys

_INPUT = """\
725




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
X = int(input())
if 400<=X<600:
    print (8)
elif 600<=X<800:
    print (7)
elif 800<=X<1000:
    print (6)
elif 1000<=X<1200:
    print (5)
elif 1200<=X<1400:
    print (4)
elif 1400<=X<1600:
    print (3) 
elif 1600<=X<1800:
    print (2)
elif 1800<=X<2000:
    print (1)