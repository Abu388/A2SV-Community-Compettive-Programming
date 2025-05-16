# Problem: Find the Longest Substring Containing Vowels in Even Counts - https://leetcode.com/problems/find-the-longest-substring-containing-vowels-in-even-counts/

class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        voule = 'aeiou'
        use = []
        for i in s:
            if i in voule:
                use.append(ord(i))
            else:
                use.append(0)
        cheker = defaultdict(int)
        maxs = 0
        cheker[use[0]] = 0
        for i in range(1,len(s)):
            use[i] ^= use[i-1]

        
        for i in range(1,len(s)):
            if  not use[i] :
                maxs = max(maxs, i + 1)
            if use[i] not in cheker:
                cheker[use[i]] = i
            
            else:
                maxs = max(maxs, (i - cheker[use[i]]) )
            

        return maxs
        