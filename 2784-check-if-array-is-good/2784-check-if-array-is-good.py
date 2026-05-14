class Solution:
    def isGood(self, nums: List[int]) -> bool:
        t = len(nums) - 1
        val = set()
        c = 0
        al = set()
        for i in range(1, len(nums)):
            al.add(i)

        for i , num in enumerate(nums):

            if num == t :
                c += 1
                continue
            
            if num not in al:
                return False
            if num in val and num != t:
                return False
            val.add(num)
        
        return True if c == 2 else False