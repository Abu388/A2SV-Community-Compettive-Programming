# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def bound(row , col):
            return 0 <= row and row < len(board) and 0 <= col and col < len(board[0])

        def dfs(row , col, visited , ind):

            dirction = [(1,0), (0,1), (-1,0), (0,-1)]
            
            if ind == len(word):
                return True

            visited.add((row,col))
            
            for r , c in  dirction:
                nr , nc = r + row ,c + col
                if bound(nr ,nc) and (nr , nc) not in visited:                    
                    if board[nr][nc] == word[ind]:                        
                        if dfs(nr , nc , visited  , ind + 1 ):
                            return True
                            
            visited.remove((row,col))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if board[i][j] == word[0]: 
                    visited = set()                    
                    if dfs(i ,j , visited , 1 ):
                        return True
                    

        return False
        









      