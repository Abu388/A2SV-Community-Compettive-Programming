# Problem: D - Lakes in Bahirdar - https://codeforces.com/gym/602812/problem/D

import sys
import threading

def solve():
    n, m, k = map(int, input().split())
    grid = [input() for _ in range(n)]

    def is_border(x, y):
        return x == 0 or y == 0 or x == n - 1 or y == m - 1

    def in_bounds(x, y):
        return 0 <= x < n and 0 <= y < m

    def dfs(x, y):
        vis.add((x, y))
        nonlocal size, is_lake, lake_cells
        lake_cells.add((x, y))
        if is_border(x, y):
            is_lake = False
        size += 1

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if in_bounds(nx, ny) and (nx, ny) not in vis and grid[nx][ny] == ".":
                dfs(nx, ny)

    vis = set()
    lakes = []
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] == "." and (i, j) not in vis:
                size = 0
                is_lake = True
                lake_cells = set()
                dfs(i, j)
                if is_lake:
                    lakes.append([size, lake_cells])

    lakes.sort()
    to_fill = len(lakes) - k
    cnt = 0

    ans = [list(row) for row in grid]
    for i in range(to_fill):
        cnt += lakes[i][0]
        for x, y in lakes[i][1]:
            ans[x][y] = "*"

    print(cnt)
    for row in ans:
        print("".join(row))

input = lambda: sys.stdin.readline().strip()

def main():
    solve()

if __name__ == '__main__':
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)
    threading.Thread(target=main).start()

