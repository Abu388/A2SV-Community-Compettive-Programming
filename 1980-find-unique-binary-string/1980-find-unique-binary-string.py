class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        hahs = set(nums)
        def backtraking(i , cur):
            if i == len(nums):
                res = ''.join(cur)
                return None if res in hahs else res
            res = backtraking(i + 1 , cur)
            if res: return res
            cur[i] = "1"

            res = backtraking(i + 1 , cur)
            if res: return res
        return backtraking(0 , ["0"] * len(nums))