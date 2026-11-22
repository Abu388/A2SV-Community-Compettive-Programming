class Solution:
    def checkString(self, s: str) -> bool:
        starts_w = True
        if s[0] == 'b':
            starts_w = False
        if starts_w:
            for i in range(1, len(s)):
                if s[i - 1] == 'b' and s[i] == 'a':
                    return False
        else:
            for i in range(len(s)):
                if s[i] == 'a':
                    return False
        
        return True