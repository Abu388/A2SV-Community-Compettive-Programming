class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        r, c = len(grid), len(grid[0])
        res = [[0]*c for _ in range(r)]
        arr = deque([])
        for i in range(r):
            for j in range(c):
                arr.append(grid[i][j])
        for _ in range(k):
            p = arr.pop()
            arr.appendleft(p)
        l = 0
        for i in range(r):
            for j in range(c):
                res[i][j] = arr[l]
                l += 1
        return res


        