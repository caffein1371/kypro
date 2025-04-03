##########################################
import io
import sys

_INPUT = """\
10
68 3
17 2
99 2
92 4
82 4
10 3
100 2
78 1
3 1
35 4


"""
sys.stdin = io.StringIO(_INPUT)
##########################################

N = int(input())
beans = []
for _ in range(N):
    Ai, Ci = map(int, input().split())
    beans.append((Ci, Ai))

# 色ごとのおいしさの最小値を保持するディクショナリ
min_taste_by_color = {}

# 最小値を計算
for color, taste in beans:
    if color in min_taste_by_color:
        min_taste_by_color[color] = min(min_taste_by_color[color], taste)
    else:
        min_taste_by_color[color] = taste

# 最小値の最大値を求める
max_min_taste = max(min_taste_by_color.values())

print(max_min_taste)