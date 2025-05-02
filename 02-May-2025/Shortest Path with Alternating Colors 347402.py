# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        blue =  defaultdict(list)
        merg = defaultdict(lambda : [[], []])
        ans = [-1] * n
        ans[0] = 0
        
        red = defaultdict(list)
        for u , v in redEdges:
            red[u].append(v)
        for u , v in blueEdges :
            blue[u].append(v)
        
        for key in red:
            merg[key] = [red[key],blue[key]]

        for key in blue:
            merg[key] = [red[key],blue[key]]
        
        # red while
        q=deque([0])
        ind = 0
        count = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                c = q.popleft()
                if ans[c] != -1:
                    ans[c] = min(count,ans[c])
                else:
                    ans[c] = count
                for i in merg[c][ind]:
                    if (i, ind) not in visited:  
                        q.append(i) 
                        visited.add((i, ind))            
            if ind == 1:
                ind = 0
            else:
                ind = 1
            count += 1

        # blue while
        q=deque([0])
        ind = 1
        count = 0
        visited = set()
        while q:
            for _ in range(len(q)):
                c = q.popleft()
                if ans[c] != -1:
                    ans[c] = min(count,ans[c])
                else:
                    ans[c] = count
                for i in merg[c][ind]:
                    if (i, ind) not in visited:  
                        q.append(i) 
                        visited.add((i, ind))   
            if ind == 1:
                ind = 0
            else:
                ind = 1
            count += 1

        return ans
