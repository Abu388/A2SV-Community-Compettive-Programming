class Solution:
    def minOperations(self, s: str) -> int:
        #start with one, one is even,b/c of zero
        one = 0
        for i in range(len(s)):            
            if i % 2 == 0 and s[i] != '1':
                one += 1
            if i % 2 != 0 and s[i] != '0':
                one += 1
        zero = 0
        for i in range(len(s)):
            
            if i % 2 == 0 and s[i] != '0':
                zero += 1
            if i % 2 != 0 and s[i] != '1':
                zero += 1

    
        return min(zero , one)

    
