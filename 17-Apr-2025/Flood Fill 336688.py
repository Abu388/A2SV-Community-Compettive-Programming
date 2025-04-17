# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = deque([])
        def inbound(row , col):
            return 0 <= row < len(image) and 0 <= col < len(image[0])
        q.append((sr,sc))
        visited = set()
        visited.add((sr,sc))
        m = image[sr][sc]
        d  = [(0,1),(1,0),(-1,0),(0,-1)]
        while q:
            r , c  = q.popleft()
            for nr , nc in d:
                newr , newc = r + nr , nc + c
                if inbound(newr,newc):
                    if image[newr][newc] == m and (newr,newc) not in visited:
                        visited.add((newr,newc))
                        q.append((newr,newc))
        for i , j in visited:
            image[i][j] = color
        return image
        


        
