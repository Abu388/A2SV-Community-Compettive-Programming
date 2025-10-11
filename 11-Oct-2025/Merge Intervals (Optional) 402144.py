# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort()
        print(intervals)
   
        for start , end in intervals:
            if not res:
                res.append([start , end])
            else:
                
                if start > res[-1][1] and start > res[-1][0] and end > res[-1][1]:
                    res.append([start , end])
                else:
                    s , e = res.pop()
                    res.append([min(s , start), max(e , end)])


        return res