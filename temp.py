##########################################
import io
import sys

_INPUT = """\
1 1000000000




"""
sys.stdin = io.StringIO(_INPUT)
##########################################
t,N = map(int,input().split())

temp = [1]*(100+t)
ans = []
for i in range(100):
    #整数型の切り捨て除算を用いて、(100+t)×A を 100 で割る形でf(A) を計算する
    temp[((t+100)*i)//100]=0
#print (temp)
for i in range(100+t):
    if temp[i]==1:
        ans.append(i)
#print (ans)

q,mod = divmod(N-1,t)
answer = q*(t+100)+ans[mod]
print (answer)
