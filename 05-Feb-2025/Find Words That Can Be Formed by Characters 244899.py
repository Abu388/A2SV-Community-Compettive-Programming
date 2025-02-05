# Problem: Find Words That Can Be Formed by Characters - https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/

from collections import Counter
class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        c = Counter(chars)  # character frequency of chars
        
        value=0
       
        for i in words:
            word_count = Counter(i) 
            if all(word_count[j]<=c[j] for j in word_count):
                value+=len(i)
        return value


        