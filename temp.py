##########################################
import io
import sys

_INPUT = """\
1 2 9 1



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N= list(map(int,input().split()))
temp=[1,7,9,4]
ans=[]
for i in range(len(N)):
        if N[i] in temp:
                ans.append(N[i])
ans = list(set(ans))
if len(ans)==4:
        print ("YES")
else:
        print ("NO")
