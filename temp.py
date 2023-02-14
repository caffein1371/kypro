##########################################
import io
import sys

_INPUT = """\
10
1 8 4 15 7 5 7 5 8 0
20
2 7 0
3 7
3 8
1 7
3 3
2 4 4
2 4 9
2 10 5
1 10
2 4 2
1 10
2 3 1
2 8 11
2 3 14
2 1 9
3 8
3 8
3 1
2 6 5
3 7






"""
sys.stdin = io.StringIO(_INPUT)
##########################################
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
g = 0
base = 0
diff = defaultdict(int)

q = int(input())
for i in range(q):
    t = list(map(int, input().split()))
    if t[0] == 1:
        #gをインクリメント
        g += 1
        #初期化する値を記憶
        base = t[1]
    elif t[0] == 2:
        #
        diff[(g, t[1])] += t[2]
    else:
        if g > 0:
            print(base + diff[(g, t[1])])
        else:
            print(a[t[1] - 1] + diff[(g, t[1])])
