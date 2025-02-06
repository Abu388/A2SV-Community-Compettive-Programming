# Problem: Transpose Matrix - https://leetcode.com/problems/transpose-matrix/

class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        
        arr=[]
        for i in range(len(matrix[0])):
            res=[]
            for j in range(len(matrix)):
                res.append(matrix[j][i])
            arr.append(res)
        return arr