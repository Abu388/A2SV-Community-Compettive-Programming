class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        pdiagon = set()
        ndiagon = set()
        res = 0
        def back(r):
            if n == r:
                nonlocal res
                res += 1
                return
            
            for c in range(n):
                if c in col or (r + c ) in pdiagon or (r - c) in ndiagon:
                    continue
                col.add(c)
                pdiagon.add(r + c)
                ndiagon.add(r - c)
                back(r + 1)
                col.remove(c)
                pdiagon.remove(r + c)
                ndiagon.remove(r - c)
        back(0)
        return res