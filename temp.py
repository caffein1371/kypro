##########################################
import io
import sys

_INPUT = """\
18278







"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
abc= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
mod = 26
amari = -1
iter = 0
# if N==1:
#         print ('a')
#         exit()

# while mod**iter<N:
#         iter+=1
# #print (iter)
ans = []
# for i in range(iter,-1,-1):
#         #print (i)
#         N,temp = divmod(N,mod)
#         temp-=1
#         ans.append(abc[temp])
        
while N!=0:
        N-=1
        M = N%mod
        ans.append(abc[M])
        N=N//mod
print(''.join(ans[::-1]))