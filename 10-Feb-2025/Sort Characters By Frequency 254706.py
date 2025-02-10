# Problem: Sort Characters By Frequency - https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        has = {}
        ans=''
     
        for i in s:
            has[i] = has.get(i, 0) + 1

        res = (sorted(has.items(), key=lambda item: item[1] ,reverse=True))

        for k,v in res:

            ans+=k*v
        return ans
        
