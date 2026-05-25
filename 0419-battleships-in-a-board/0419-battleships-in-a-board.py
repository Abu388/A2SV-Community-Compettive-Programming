class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        res = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if 'X' != board[r][c]:
                    continue
                if r - 1 >= 0 and board[r - 1][c] == 'X':
                    continue
                if c - 1 >= 0 and board[r][c - 1] == 'X':
                    continue
                res += 1
        return res
                