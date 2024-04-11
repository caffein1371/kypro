##########################################
import io
import sys

_INPUT = """\
2 2
S.
T.
1
1 2 4


"""
sys.stdin = io.StringIO(_INPUT)
##########################################
from collections import deque

def is_valid_move(grid, visited, energy, x, y):
    H, W = len(grid), len(grid[0])
    return 0 <= x < H and 0 <= y < W and grid[x][y] != '#' and not visited[x][y][energy]

def bfs(grid, start_x, start_y, target_x, target_y, energies):
    H, W = len(grid), len(grid[0])
    max_energy = max(energies, key=lambda x: x[2])[2]  # 最大エネルギーを取得
    visited = [[[False] * (max_energy + 1) for _ in range(W)] for _ in range(H)]
    queue = deque([(start_x, start_y, 0)])  # (x, y, energy)
    visited[start_x][start_y][0] = True

    while queue:
        x, y, energy = queue.popleft()

        if x == target_x and y == target_y:
            return True
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_x, new_y = x + dx, y + dy
            
            if is_valid_move(grid, visited, energy, new_x, new_y):
                if grid[new_x][new_y] == 'T':
                    return True

                new_energy = energy
                if (new_x, new_y) in energies:
                    idx = energies.index((new_x, new_y))
                    new_energy = energies[idx][2]

                visited[new_x][new_y][new_energy] = True
                queue.append((new_x, new_y, new_energy))
    
    return False

if __name__ == "__main__":
    H, W = map(int, input().split())  # Input grid size
    grid = [list(input()) for _ in range(H)]  # Input grid
    N = int(input())  # Number of medicines
    
    energies = []
    for _ in range(N):
        r, c, e = map(int, input().split())  # Input medicine positions and energies
        energies.append((r - 1, c - 1, e))
    
    # Find start and target positions
    start_x, start_y, target_x, target_y = None, None, None, None
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'S':
                start_x, start_y = i, j
            elif grid[i][j] == 'T':
                target_x, target_y = i, j
    
    # Perform BFS
    if bfs(grid, start_x, start_y, target_x, target_y, energies):
        print("Yes")
    else:
        print("No")
