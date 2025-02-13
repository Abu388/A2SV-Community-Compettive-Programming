# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s =='' :
            return 0
        l=0
        count=1
        arr=[]
        while l<len(s):
            if s[l] not in arr:
                arr.append(s[l])
                count=max(count,len(arr))

                l+=1

            else:
                arr.pop(0)
        return count
        

            
        