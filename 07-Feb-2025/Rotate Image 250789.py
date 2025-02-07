# Problem: Rotate Image - https://leetcode.com/problems/rotate-image/

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        dec={}
        ind=0
        for j in range(len(matrix)):
            res=[]
            for i in range(len(matrix)-1,-1,-1):
                print(matrix[i][j])
                res.append(matrix[i][j])
            dec[ind]=tuple(res)
            ind+=1
        for keys, values in dec.items():
            matrix[keys]=list(values)
        return matrix

                 



#print(j,i)
 #   print(matrix[j][i])



    
                