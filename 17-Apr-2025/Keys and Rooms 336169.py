# Problem: Keys and Rooms - https://leetcode.com/problems/keys-and-rooms/

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        visited.add(0)
        q = deque()
        for i in rooms[0]:
            q.append(i)
            visited.add(i)

        while q:
        
            l = q.popleft()
           
            for chiled in rooms[l]:
                if chiled not in visited:
                    visited.add(chiled)
                    q.append(chiled)
        
        if len(visited) == len(rooms):
            return True
        return False

        