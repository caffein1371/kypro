##########################################
import io
import sys

_INPUT = """\
4
0 0
2 4
5 0
3 4


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def max_distance_point(points):
    max_distances = []
    for i, (x1, y1) in enumerate(points):
        max_distance = float('-inf')
        max_distance_point = None
        for j, (x2, y2) in enumerate(points):
            if i != j:
                dist = distance(x1, y1, x2, y2)
                if dist > max_distance:
                    max_distance = dist
                    max_distance_point = j + 1
        max_distances.append(max_distance_point)
    return max_distances

# 座標の数を入力
N = int(input())
points = []
# 座標を入力
for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

result = max_distance_point(points)
for point in result:
    print(point)
    