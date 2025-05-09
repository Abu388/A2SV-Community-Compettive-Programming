# Problem: Single-Threaded CPU - https://leetcode.com/problems/single-threaded-cpu/


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:        
        n = len(tasks)
        indexed_tasks = [(enqueue, process, idx) for idx, (enqueue, process) in enumerate(tasks)]

        indexed_tasks.sort()
        
        result = []
        min_heap = []
        time = 0
        i = 0 
        while i < n or min_heap:
            while i < n and indexed_tasks[i][0] <= time:
                enqueue, process, idx = indexed_tasks[i]
                heapq.heappush(min_heap, (process, idx))  
                i += 1
        
            if min_heap:
                
                proc_time, idx = heapq.heappop(min_heap)
                time += proc_time
                result.append(idx)
            else:
               
                time = indexed_tasks[i][0]
        
        return result
