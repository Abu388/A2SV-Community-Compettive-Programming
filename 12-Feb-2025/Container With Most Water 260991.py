# Problem: Container With Most Water - https://leetcode.com/problems/container-with-most-water/

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l,r=0,len(height)-1
        res=float('-inf')
        while l<r:
            mini=min(height[l],height[r])
            res=max(res,mini*(r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        return res

        