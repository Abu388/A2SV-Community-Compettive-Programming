# Problem: Course Schedule IV - https://leetcode.com/problems/course-schedule-iv/description/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        value = set()
        res = []
        for pre , cor in prerequisites:
            graph[pre].append(cor)
            
            value.add(pre)
            
    
        def dfs(node,ser):
            if node == ser:

                
                return True
            for chiled in graph[node]:
                if chiled not in visited:
                    visited.add(chiled)
                    if dfs(chiled, ser):
                        return True

            
            return False

                 

        for org , ser in queries:
            
            if org in value:
                visited = set() 

                if not dfs(org,ser):
                    res.append(False)  
                else:
                    res.append(True)                
                
            else:
                res.append(False)

        return res
        