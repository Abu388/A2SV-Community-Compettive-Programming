# Problem: Minesweeper - https://leetcode.com/problems/minesweeper/

class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        rows, cols = len(board), len(board[0])
        directions = [(0,1), (1,0), (-1,0), (0,-1), (-1,-1), (-1,1), (1,-1), (1,1)]

        def in_bounds(r, c):
            return 0 <= r < rows and 0 <= c < cols

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        q = deque()
        q.append((click[0], click[1]))
        visited = set()

        while q:
            r, c = q.popleft()
            if (r, c) in visited:
                continue
            visited.add((r, c))

            mines = 0
            neighbors = []
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if in_bounds(nr, nc):
                    if board[nr][nc] == 'M':
                        mines += 1
                    else:
                        neighbors.append((nr, nc))
            
            if mines > 0:
                board[r][c] = str(mines)
            else:
                board[r][c] = 'B'
                for nbr in neighbors:
                    if nbr not in visited:
                        q.append(nbr)

        return board
