class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:

        nums.sort()
        num_set = set(nums)
        max_streak = 0

        for num in nums:
            streak = 0
            current = num
            
            while current in num_set:
                streak += 1
                current *= current  

            
            if streak >= 2:
                max_streak = max(max_streak, streak)

        return max_streak if max_streak >= 2 else -1

        
        
        
    
    