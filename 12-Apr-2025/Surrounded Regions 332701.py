# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        arr = []
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != 'O':
                return
           
            board[i][j] = 'T'             
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        rows  = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                if (i in (0, rows - 1) or j in (0, cols - 1)) and board[i][j] == 'O':
                    dfs(i, j)
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] ='X'
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'T':
                    board[i][j] = 'O'

             
                                          
                                
