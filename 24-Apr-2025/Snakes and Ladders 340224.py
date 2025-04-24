# Problem: Snakes and Ladders - https://leetcode.com/problems/snakes-and-ladders/

from collections import deque

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)

        def get_coords(s):
            row = (s - 1) // n
            col = (s - 1) % n
            real_row = n - 1 - row
            real_col = col if row % 2 == 0 else n - 1 - col
            return real_row, real_col

        visited = set()
        q = deque()
        q.append((1, 0))  
        visited.add(1)

        while q:
            square, moves = q.popleft()
            if square == n * n:
                return moves

            for i in range(1, 7):  
                next_square = square + i
                if next_square > n * n:
                    continue
                r, c = get_coords(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]

                if next_square not in visited:
                    visited.add(next_square)
                    q.append((next_square, moves + 1))

        return -1
