##########################################
import io
import sys

_INPUT = """\
10
in that1 case you1 should print yes and1 not1 no






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
S =input()
Wlist = S.split()
#print (Wlist)
temp = ['and','not','that','the','you']
for i in range(N):
    for j in range(5):
        if Wlist[i]==temp[j]:
            print ('Yes')
            #print (i,j)
            quit()
print ('No')

