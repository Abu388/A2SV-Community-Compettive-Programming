# Problem: Group Anagrams - https://leetcode.com/problems/group-anagrams/

from collections import Counter, defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]+
        """
        groups = defaultdict(list)
        

        for word in strs:
            count = tuple(sorted(Counter(word).items()))  
            groups[count].append(word)

        return list(groups.values())

        
                