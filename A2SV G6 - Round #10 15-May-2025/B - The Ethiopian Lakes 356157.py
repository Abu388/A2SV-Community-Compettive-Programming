# Problem: B - The Ethiopian Lakes - https://codeforces.com/gym/602812/problem/B

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    
    max_volume = 0
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    for i in range(n):
        for j in range(m):
            if grid[i][j] > 0 and not visited[i][j]:
                stack = [(i, j)]
                visited[i][j] = True
                volume = 0

                while stack:
                    x, y = stack.pop()
                    volume += grid[x][y]

                    for dx, dy in directions:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < n and 0 <= ny < m:
                            if not visited[nx][ny] and grid[nx][ny] > 0:
                                visited[nx][ny] = True
                                stack.append((nx, ny))
                
                max_volume = max(max_volume, volume)
    
    print(max_volume)