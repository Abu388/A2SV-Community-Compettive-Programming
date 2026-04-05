class Solution:
    def judgeCircle(self, moves: str) -> bool:
        u = r = 0
        for n in moves:
            if n == 'U':
                u += 1
            elif n == 'D':
                u -= 1
            elif n == 'R':
                r += 1
            else:
                r -= 1
        return r == 0 and u == 0