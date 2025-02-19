# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        if firstList==[] or secondList==[]:
            return []
        arr=[]
        j,i=0,0
        while i < len(firstList) and j < len(secondList):
            start, end = firstList[i]
            s, e = secondList[j]
            
            if start > e:
                j += 1  
            elif s > end:
                i += 1  
            else:
                arr.append([max(start, s), min(end, e)])
                if end < e:
                    i += 1
                else:
                    j += 1
        
        return arr
           
           
           
           
     

