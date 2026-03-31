class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        res = []
        for i in range(len(boxes)):
            r = len(boxes) - 1
            c = 0
            while r > i:
                if boxes[r] == '1':
                    c += r - i
                r -= 1
            l = 0
            while l < i:
                if boxes[l] == '1':
                    c += i - l
                l += 1
            res.append(c)
        return res
