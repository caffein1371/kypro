##########################################
import io
import sys

_INPUT = """\
4 5



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
R,C = map(int,input().split())
if R==1 or C==1 or R==15 or C==15:
    print ("black")
elif R==2 or C==2 or R==14 or C==14:
    print ("white")
elif R==3 or C==3 or R==13 or C==13:
    print ("black")
elif R==4 or C==4 or R==12 or C==12:
    print ("white")
elif R==5 or C==5 or R==11 or C==11:
    print ("black")
elif R==6 or C==6 or R==10 or C==10:
    print ("white")
elif R==7 or C==7 or R==9 or C==9:
    print ("black")
elif R==8 or C==8 or R==8 or C==8:
    print ("white")