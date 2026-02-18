class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        

        flag = False
        l = 0
        r = len(nums)-1
        mid = (r+l)//2
        while l<=r:
            if nums[mid] < target:
                l = mid +1
            elif nums[mid] > target:
                r = mid - 1
            else:
                flag = True
                break
            mid = (r+l)//2

        if not flag:
            return [-1,-1]
        
        hig = mid
        lef = mid
        
        while hig < len(nums) and nums[hig] == target:
            hig += 1
        while lef >= 0 and nums[lef] ==  target:
            lef -= 1

        return [lef+1,hig-1]
