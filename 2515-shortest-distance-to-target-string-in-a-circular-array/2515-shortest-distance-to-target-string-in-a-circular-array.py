class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n = len(words)
        if target not in words:
            return -1
        r = startIndex 
        cr = 0
        while words[r]  != target:
            r = (r + 1) % n
            cr += 1
        l = startIndex 
        cl = 0
        while words[l]  != target:
            l = (l - 1 + n) % n
            cl += 1
        return min(cl, cr)