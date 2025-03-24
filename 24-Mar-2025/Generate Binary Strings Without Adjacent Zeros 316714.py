# Problem: Generate Binary Strings Without Adjacent Zeros - https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/description/

class Solution:
    def validStrings(self, n: int) -> List[str]:
        ans = []
        def solu( s):
            if len(s) == n:
                ans.append(s)
                return
            solu( s +'1')
            if not s or s[-1] ==  '1':
                solu(s + '0')
            
        solu("")
        return ans