##########################################
import io
import sys

_INPUT = """\
3
3
1
2





"""
sys.stdin = io.StringIO(_INPUT)
##########################################
N = int(input())
ans = []
for i in range(N):
    a = int(input())
    a-=1
    ans.append(a)
tansaku = set()
temp = 0
i = 1
while True:
    if ans[temp]==1:
        print (i)
        break
    if ans[temp] not in tansaku:
        tansaku.add(ans[temp])
        #tansaku = liset(tansaku))

    else:
        print (-1)
        break
    temp = ans[temp]
    i+=1


    