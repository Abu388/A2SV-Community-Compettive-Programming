# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        
        nums=[]
        val=int(c**0.5)+1
        for i in range(val):
            nums.append(i)
        l,r=0,len(nums)-1
        print(nums)
        while l<=r:
            res=nums[l]**2 +nums[r]**2
            if res>c:
                r-=1
            elif res<c:
                l+=1
            else:
                return True
        return False
    

