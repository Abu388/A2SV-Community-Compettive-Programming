class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        b , t =0, len(arr)
        if start < b or start > t:
            return False
        q = deque([(arr[start], start)])
        visited = set()
        def inbound(index):
            return 0<= index < t
        while q:
            val ,ind = q.popleft()
            if ind in visited:
                continue

            if val == 0:
                return True
            visited.add(ind)
            n = arr[ind]
            if inbound(n + ind) :
                q.append((arr[n + ind], n + ind))
                
            if inbound(ind - n ):
                q.append((arr[ind - n], ind - n))  

        return False

