# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stk , val = [], []
        for i in range(len(pattern)+1):
            val.append(i+1)
            while val and (i == len(pattern) or pattern[i]=='I'):
                stk.append(str(val.pop()))
        return ''.join(stk)
