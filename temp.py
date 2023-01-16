##########################################
import io
import sys

_INPUT = """\
6
abcbac


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N= int(input())
S = input()

#iは何個スキップするか
#MaxでN-1スキップ
for i in range(1,N):
    for j in range(1,N+1):
        #最後まで見つからなかった場合
        if i+j>N:
            print (j-1)
            break
        #途中で見つかった場合
        #print (S[j-1],S[i+j-1])
        if S[j-1]==S[i+j-1]:
            print (j-1)
            break