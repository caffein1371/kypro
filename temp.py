##########################################
import io
import sys

_INPUT = """\
10
5 4 3 2 1 0 7 7 6 6



"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
plist = list(map(int,input().split()))
#2*10**5
temp = [0 for i in range(210001)]
iter =0
for i in range(N):
        #plistの
        temp[plist[i]]+=1
        #iterから探索を始める
        #tempが0であれば，whileから抜ける
        #以下のループで既に使われたかどうかを判定する
        while temp[iter]!=0:
                iter+=1
        print (iter)