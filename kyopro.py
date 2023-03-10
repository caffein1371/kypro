##########################################
import io
import sys

_INPUT = """\
10
1 2 3 4 5 6 7 8 9



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
#人１が人Nの何代前か求めてください
N = int(input())
Plist = [0]+list(map(int,input().split()))

ans = 0
temp = Plist[-1]
#print (temp)
while temp!=0:
    temp= Plist[temp-1]
    ans+=1
    
print (ans)