class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        r = l = d = 0

        for m in moves:
            if m == 'L':
                l += 1
            elif m == 'R':
                r += 1
            else:
                d += 1
        
        if r > l:
            return r + d - l
        return l + d - r
