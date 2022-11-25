##########################################
import io
import sys

_INPUT = """\
2 12


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
n,x= map(int,input().split())
temp = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
ans = []
for i in range(26):
    for j in range(n):
        ans.append(temp[i])
print(ans[x-1])
