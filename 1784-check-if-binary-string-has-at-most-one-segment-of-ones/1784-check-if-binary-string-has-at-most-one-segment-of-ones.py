class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        flag = True
        for i in s:
            if i == '1' and flag:
                continue
            if i == '0':
                flag = False
            if i == '1' and not flag:
                return False
        return True