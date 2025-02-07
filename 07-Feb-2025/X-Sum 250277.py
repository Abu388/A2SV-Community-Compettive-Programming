# Problem: X-Sum - https://codeforces.com/problemset/problem/1676/D

def solution(arr):
    row, col = len(arr), len(arr[0])
    res = 0
    directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

    for r in range(row):
        for c in range(col):
            total_sum = arr[r][c]

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                while 0 <= nr < row and 0 <= nc < col:
                    total_sum += arr[nr][nc]
                    nr += dr
                    nc += dc

            res = max(total_sum,res)   

    return res


t = int(input())

for _ in range(t):
    row, col = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(row)]
    print(solution(arr))
