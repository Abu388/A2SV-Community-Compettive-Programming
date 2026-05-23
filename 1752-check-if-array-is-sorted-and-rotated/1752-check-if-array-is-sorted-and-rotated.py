class Solution:
    def check(self, nums: List[int]) -> bool:
        N=len(nums)
        r=sorted(nums)

        for i in range (N):
            if nums[i:] + nums[:i] == r:
                return True
            
        return False

        