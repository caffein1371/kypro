##########################################
import io
import sys

_INPUT = """\
4 4
S...
#..#
#...
..#T
4
1 1 3
1 3 5
3 2 1
2 3 1

"""
sys.stdin = io.StringIO(_INPUT)
##########################################
def dfs(grid, visited, energy, start_i, start_j, target_i, target_j):
    # ゴール地点に到達した場合、エネルギーが0以上ならばTrueを返す
    if start_i == target_i and start_j == target_j:
        return energy >= 0
    
    # 現在地を訪問済みとしてマーク
    visited[start_i][start_j] = True

    # 上下左右の移動を試みる
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        ni, nj = start_i + di, start_j + dj
        # グリッドの範囲内かつ障害物でなく、未訪問の空きマスの場合
        if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and not visited[ni][nj] and grid[ni][nj] != '#':
            # エネルギーが0以上の場合、再帰的に探索を行う
            if dfs(grid, visited, energy - 1, ni, nj, target_i, target_j):
                return True

    return False

def can_reach_target(grid, start_i, start_j, target_i, target_j):
    # グリッドのサイズ
    H, W = len(grid), len(grid[0])
    
    # 訪問状態を管理する配列
    visited = [[False] * W for _ in range(H)]
    
    # DFSを実行してゴール地点に到達可能かどうかを判定
    return dfs(grid, visited, 0, start_i, start_j, target_i, target_j)

# グリッドのサイズを受け取る
H, W = map(int, input().split())

# グリッドを受け取る
grid = [input() for _ in range(H)]

# スタート地点とゴール地点を探す
start_i, start_j = 0, 0
target_i, target_j = 0, 0
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            start_i, start_j = i, j
        elif grid[i][j] == 'T':
            target_i, target_j = i, j

# スタート地点からゴール地点まで到達可能かどうかを判定
if can_reach_target(grid, start_i, start_j, target_i, target_j):
    print("Yes")
else:
    print("No")
