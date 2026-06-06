class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = [0]
        r = [0] 
        for i in range(len(nums) - 1):
            left.append(left[i] + nums[i ])
        j = 0
        print(left)
        for i in range(len(nums) - 1, 0 , -1):
            r.append( nums[i] + r[j])
            j += 1
        r = r[::-1]
        for i in range(len(left)):
            left[i] = abs(left[i] - r[i])
        
        return left
        