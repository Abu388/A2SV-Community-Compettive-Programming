# Problem: Minimum Processing Time - https://leetcode.com/problems/minimum-processing-time/

class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        tasks.sort(reverse=True)
 
        processorTime.sort()
        arr=[]
        l,ind=0,0
        while l<len(processorTime):
            res = max(tasks[ind:ind + 4])
            arr.append(res+processorTime[l])

            ind+=4
            l+=1
        final=max(arr)
        return final




    