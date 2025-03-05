# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])
        
        arrows = 1
        last_arrow_position = points[0][1]
        
        for start, end in points[1:]:
            if start > last_arrow_position:
                arrows += 1
                last_arrow_position = end
        
        return arrows

