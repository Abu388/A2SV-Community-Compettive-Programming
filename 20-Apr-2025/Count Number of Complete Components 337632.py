# Problem: Count Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()  
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
    
        def helper(node):
            
            if len(stk)-1 != len(graph[node]):
                return False 
            for chiled in graph[node]:                
                if chiled not in helper_stk:
                    helper_stk.add(chiled)                    
                    if not helper(chiled): return False
            return True              
               
        def dfs(node,stk): 
            

            for chiled in graph[node]:
                if chiled not in visited:
                    stk.add(chiled)
                    visited.add(chiled)
                    dfs(chiled,stk)
            return 
     
        count = 0
        for i in range(n):
            if i in graph:
                if i not in visited:
                    
                    stk = set()
                    dfs(i,stk)  
                    helper_stk = set()                  
                    if helper(i):

                        count += 1
                        
                    
                        
            else:
                count += 1
            
        return count