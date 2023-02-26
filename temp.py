##########################################
import io
import sys

_INPUT = """\
5
RLURU




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
S = input()
x,y = 0,0
flag = False
ans = ([[0,0]])
iter = 1
for i in range(N):
        if S[i]=='U':
                y+=1
        elif S[i]=='R':
                x+=1
        elif S[i]=='L':
                x-=1
        elif S[i]=='D':
                y-=1
        
        # if [x,y] in ans :
        #         flag = True
        #         break
        ans.append([x,y])
        iter+=1
arr = list(map(list, set(map(tuple, ans))))
# print (arr)
# print (iter)
if iter!=len(arr):
        print ('Yes')
else:
        print ('No')
