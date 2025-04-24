# Problem: Predict the Winner - https://leetcode.com/problems/predict-the-winner/

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def solu(left,right):
            if left == right:
                return nums[right]
            pl = nums[left] - solu(left+1,right)
            pr = nums[right] - solu(left,right-1)
            return max(pl,pr)
        return solu(0,len(nums)-1) >= 0