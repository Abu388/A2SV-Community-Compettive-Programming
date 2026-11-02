class Solution:

  def minMoves(self, nums: List[int]) -> int:
    min_val = min(nums)
    return sum(nums) - len(nums) * min_val