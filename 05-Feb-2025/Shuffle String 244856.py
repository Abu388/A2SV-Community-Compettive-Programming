# Problem: Shuffle String - https://leetcode.com/problems/shuffle-string/description/

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        has={}
        res=''
        ind=0
        for i in s:
            has[indices[ind]]=i
            ind+=1
        for j in range(len(indices)):
            res+=has[j]
        return res
        

        