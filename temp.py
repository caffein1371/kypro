##########################################
import io
import sys

_INPUT = """\
45
tgxgdqkyjzhyputjjtllptdfxocrylqfqjynmfbfucbir


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
S = input()

Ans = -1
for i in range(1,N+1):
    temp1 = S[0:i]
    temp2 = S[i:]
    temp1 = set(temp1)
    temp2 = set(temp2)
    ans = 0
    for i in temp1:
        for j in temp2:
            if i==j:
                ans+=1
    Ans = max(ans,Ans)
print (Ans)



