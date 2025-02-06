# Problem: Valid Sudoku - https://leetcode.com/problems/valid-sudoku/

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row=0
        column=0
        
        while column < 9 and row < 9:  # fixed loop range
            column_check = {}
            row_check = {}
            for i in range(9):  # iterate only within 9x9 bounds
                if board[row][i] != ".":
                    row_check[board[row][i]] = row_check.get(board[row][i], 0) + 1
                    if row_check[board[row][i]] > 1:  # check row duplicates correctly
                        return False

                if board[i][column] != ".":
                    column_check[board[i][column]] = column_check.get(board[i][column], 0) + 1
                    if column_check[board[i][column]] > 1:  # check column duplicates correctly
                        return False

            row += 1
            column += 1
        row=0
        column=0
        
        while column<9:
            row =0
            while row<9:
                matrix_check={}
                for r in range(row,row+3):
                    for c in range(column,column+3):
                        if board[r][c] != ".":
                            matrix_check[board[r][c]]=matrix_check.get(board[r][c],0)+1
                            if matrix_check[board[r][c]] > 1:
                                return False


                row+=3
            column+=3

        return True

            
