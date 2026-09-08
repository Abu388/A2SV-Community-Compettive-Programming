class Solution(object):
    def countCommas(self, n):
        """
        :type n: int
        :rtype: int
        """
        val = str(n)
        if len(val) <= 3:
            return 0
        
        return (n - 1000) + 1